// File:          <ClassName>.cs
// Namespace:     <Solution>.<Layer>
// Purpose:       <One-line description of this class's single responsibility>
// Prerequisites: Registered in the DI container (see Program.cs or the relevant
//                IServiceCollection extension method).
// Dependencies:  <Package A> (<NuGet ID>), <Package B>

#nullable enable

namespace <Solution>.<Layer>;

/// <summary><One-sentence description of this class.></summary>
public sealed class <ClassName> : I<ClassName>
{
    private readonly I<Dependency> _dependency;
    private readonly ILogger<<ClassName>> _logger;

    public <ClassName>(I<Dependency> dependency, ILogger<<ClassName>> logger)
    {
        _dependency = dependency;
        _logger = logger;
    }

    /// <inheritdoc/>
    public async Task<<ReturnType>> <MethodName>Async(
        <ParamType> param,
        CancellationToken cancellationToken = default)
    {
        _logger.LogInformation("Starting {OperationName} for {Param}", nameof(<MethodName>Async), param);

        try
        {
            var result = await _dependency.<DependencyMethod>Async(param, cancellationToken);

            if (result is null)
            {
                throw new <DomainNotFoundException>($"<Resource> not found for param={param}");
            }

            return result;
        }
        catch (<DomainException> ex)
        {
            _logger.LogError(ex, "Operation failed. Param={Param}", param);
            throw;
        }
    }
}
