// File:      tests/<Layer>.Tests/<ClassName>Tests.cs
// Scope:     Unit — no I/O; all dependencies isolated with NSubstitute
// Framework: xUnit + NSubstitute + FluentAssertions

using FluentAssertions;
using Microsoft.Extensions.Logging.Abstractions;
using NSubstitute;
using NSubstitute.ExceptionExtensions;
using Xunit;

namespace <Solution>.<Layer>.Tests;

public sealed class <ClassName>Tests
{
    // Arrange: shared substitutes initialised once per test instance (xUnit creates
    // a new instance per [Fact]/[Theory], so no cross-test contamination).
    private readonly I<Dependency> _dependency = Substitute.For<I<Dependency>>();
    private readonly <ClassName> _sut;

    public <ClassName>Tests()
    {
        _sut = new <ClassName>(_dependency, NullLogger<<ClassName>>.Instance);
    }

    // ------------------------------------------------------------------
    // <MethodName>Async — happy path
    // ------------------------------------------------------------------

    [Fact]
    public async Task <MethodName>Async_Returns<Expected>_When<Condition>()
    {
        // Arrange
        var expected = new <ReturnType>(<values>);
        _dependency.<DependencyMethod>Async(<arg>, Arg.Any<CancellationToken>())
                   .Returns(expected);

        // Act
        var result = await _sut.<MethodName>Async(<validArg>);

        // Assert
        result.Should().BeEquivalentTo(expected);
    }

    // ------------------------------------------------------------------
    // <MethodName>Async — not-found path
    // ------------------------------------------------------------------

    [Fact]
    public async Task <MethodName>Async_Throws<NotFoundException>_When<ResourceMissing>()
    {
        // Arrange
        _dependency.<DependencyMethod>Async(Arg.Any<<ParamType>>(), Arg.Any<CancellationToken>())
                   .Returns((<ReturnType>?)null);

        // Act
        var act = () => _sut.<MethodName>Async(<missingArg>);

        // Assert
        await act.Should().ThrowAsync<<NotFoundException>>();
    }

    // ------------------------------------------------------------------
    // <MethodName>Async — dependency failure propagation
    // ------------------------------------------------------------------

    [Fact]
    public async Task <MethodName>Async_Rethrows<DomainException>_WhenDependencyFails()
    {
        // Arrange
        _dependency.<DependencyMethod>Async(Arg.Any<<ParamType>>(), Arg.Any<CancellationToken>())
                   .ThrowsAsync(new <DomainException>("<message>"));

        // Act
        var act = () => _sut.<MethodName>Async(<validArg>);

        // Assert
        await act.Should().ThrowAsync<<DomainException>>();
    }

    // ------------------------------------------------------------------
    // Parameterised cases
    // ------------------------------------------------------------------

    [Theory]
    [InlineData(<caseA_input>, <caseA_expected>)]
    [InlineData(<caseB_input>, <caseB_expected>)]
    public async Task <MethodName>Async_ReturnsExpected_ForParameterisedInputs(
        <InputType> input,
        <OutputType> expected)
    {
        // Arrange
        _dependency.<DependencyMethod>Async(input, Arg.Any<CancellationToken>())
                   .Returns(expected);

        // Act
        var result = await _sut.<MethodName>Async(input);

        // Assert
        result.Should().Be(expected);
    }
}
