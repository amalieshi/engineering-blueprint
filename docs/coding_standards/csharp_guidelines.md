# C# and .NET Coding Standards

**Applies to:** All C# projects in this portfolio  
**Target framework:** .NET 8 (LTS)  
**Language version:** C# 12  
**Enforcement:** Roslyn analyzers, `dotnet format`, `dotnet test`

---

## 1. Project Configuration Baseline

Every `.csproj` must include:

```xml
<PropertyGroup>
  <TargetFramework>net8.0</TargetFramework>
  <LangVersion>12</LangVersion>
  <Nullable>enable</Nullable>
  <ImplicitUsings>enable</ImplicitUsings>
  <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
  <AnalysisMode>All</AnalysisMode>
  <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>
</PropertyGroup>
```

`<Nullable>enable</Nullable>` is non-negotiable. Nullable warnings treated as errors. Annotate every reference type explicitly as nullable (`string?`) or non-nullable (`string`).

---

## 2. Roslyn Analyzers

Include in every project:

```xml
<ItemGroup>
  <PackageReference Include="Microsoft.CodeAnalysis.NetAnalyzers" Version="8.*" PrivateAssets="all" />
  <PackageReference Include="StyleCop.Analyzers" Version="1.2.*" PrivateAssets="all" />
  <PackageReference Include="Roslynator.Analyzers" Version="4.*" PrivateAssets="all" />
</ItemGroup>
```

Place a shared `Directory.Build.props` at the solution root to apply these to all projects without per-project repetition.

---

## 3. Nullable Reference Types

All reference-type parameters, return values, and properties must be explicitly annotated.

```csharp
// Correct
public string GetPatientName(int patientId) { ... }      // guaranteed non-null
public string? FindPatientName(int patientId) { ... }    // may return null

// Incorrect — ambiguous
public string GetPatientName(int patientId) { return null!; }  // suppressing with ! is a code smell
```

Avoid the null-forgiving operator (`!`) except when interacting with APIs that don't have nullable annotations yet (e.g., older EF Core navigation properties). Add an inline comment when you use it.

---

## 4. Async/Await Patterns

- **Every I/O operation** (database, HTTP, file) must be async. Do not use synchronous I/O in web or pipeline contexts.
- Always `await` — never `.Result` or `.Wait()` (deadlock risk in ASP.NET contexts).
- Propagate `CancellationToken` from the call site through to every awaitable method.
- Suffix all async methods with `Async`.

```csharp
public async Task<PatientRecord?> GetPatientAsync(
    int patientId,
    CancellationToken cancellationToken = default)
{
    return await _repository.FindByIdAsync(patientId, cancellationToken);
}
```

Avoid `async void` except for event handlers. Use `async Task` instead.

---

## 5. Dependency Injection

Use the built-in `Microsoft.Extensions.DependencyInjection` container. Do not use service locator pattern (`IServiceProvider.GetService<T>()` inside business logic).

```csharp
// Register in Program.cs or a dedicated extension method
services.AddScoped<IPatientRepository, PatientRepository>();
services.AddSingleton<IDataValidator, Hl7DataValidator>();

// Consume via constructor injection
public class PatientService
{
    private readonly IPatientRepository _repository;
    private readonly ILogger<PatientService> _logger;

    public PatientService(IPatientRepository repository, ILogger<PatientService> logger)
    {
        _repository = repository;
        _logger = logger;
    }
}
```

Use `AddScoped` for services that hold per-request state (most services), `AddSingleton` only for thread-safe, stateless services.

---

## 6. Error Handling

- Define domain-specific exception types in a dedicated `Exceptions/` directory.
- Do not catch `Exception` at a low level unless you re-throw or have a documented reason.
- Use `ILogger` with structured logging — not `Console.WriteLine`.

```csharp
public class RecordNotFoundException : Exception
{
    public int PatientId { get; }

    public RecordNotFoundException(int patientId)
        : base($"No record found for PatientId={patientId}")
    {
        PatientId = patientId;
    }
}
```

In ASP.NET Core, use a global exception handler middleware or `IExceptionHandler` (introduced in .NET 8) rather than try/catch in every controller action.

---

## 7. Logging

Use `Microsoft.Extensions.Logging` with structured log messages. Use `LoggerMessage.Define` or the `[LoggerMessage]` source generator for high-performance logging on hot paths.

```csharp
// Preferred for hot paths — zero allocation
[LoggerMessage(Level = LogLevel.Information, Message = "Processing record {RecordId} for patient {PatientId}")]
private static partial void LogProcessingRecord(ILogger logger, Guid recordId, int patientId);
```

For general use:

```csharp
_logger.LogWarning("Record not found. PatientId={PatientId}", patientId);
```

Never interpolate directly into log message strings — it defeats structured logging and incurs unnecessary string allocation.

---

## 8. Architecture Principles

### Clean Architecture Layers

```
src/
├── Domain/          # Entities, value objects, domain exceptions, interfaces
├── Application/     # Use cases, DTOs, service interfaces, validation
├── Infrastructure/  # EF Core, HTTP clients, external integrations
└── API / CLI /      # Entry points — thin, delegate to Application layer
    Presentation/
```

Business logic belongs in `Domain` and `Application`. `Infrastructure` and `Presentation` layers must not contain logic.

### Records and Immutability

Use `record` types for DTOs and value objects. Prefer immutable data structures.

```csharp
public sealed record PatientDto(int Id, string FullName, DateOnly DateOfBirth);
```

### Collections

- Return `IReadOnlyList<T>` or `IEnumerable<T>` from domain methods — not `List<T>`.
- Accept `IEnumerable<T>` as input parameters where possible.

---

## 9. Testing

Framework: `xUnit`  
Mocking: `Moq` or `NSubstitute`  
Coverage threshold: **80% minimum**

```csharp
public class PatientServiceTests
{
    [Fact]
    public async Task GetPatientAsync_ThrowsRecordNotFoundException_WhenPatientDoesNotExist()
    {
        // Arrange
        var mockRepo = new Mock<IPatientRepository>();
        mockRepo.Setup(r => r.FindByIdAsync(999, It.IsAny<CancellationToken>()))
                .ReturnsAsync((PatientRecord?)null);

        var service = new PatientService(mockRepo.Object, NullLogger<PatientService>.Instance);

        // Act & Assert
        await Assert.ThrowsAsync<RecordNotFoundException>(() =>
            service.GetPatientAsync(999, CancellationToken.None));
    }
}
```

Integration tests use `WebApplicationFactory<T>` for API testing and a real (in-memory or containerized) database. Never mock the database in integration tests.

---

## 10. Code Formatting

Run `dotnet format` before every commit. Configure via `.editorconfig` at the solution root. Key settings:

```ini
[*.cs]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8-bom
trim_trailing_whitespace = true
dotnet_sort_system_directives_first = true
csharp_style_namespace_declarations = file_scoped:warning
```
