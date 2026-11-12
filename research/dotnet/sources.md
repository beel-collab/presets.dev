# .NET sources

Fetched 12 November 2026.

- https://devblogs.microsoft.com/dotnet/announcing-dotnet-11/ announces .NET 11.
- https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15 documents C# 15 unions. They belong on a project that targets the runtime that ships that language version. A `net10.0` project does not get them. Do not retarget it unless asked.
- https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/9.0/binaryformatter-removal says the in-box `BinaryFormatter` implementation throws as of .NET 9. https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-migration-guide/ says to migrate, with `System.Text.Json` as one replacement.
