# SwiftUI sources

Fetched 12 November 2026.

- https://www.swift.org/blog/swift-6.4-released/ (15 September 2026) documents async `defer` (SE-0493), `withTaskCancellationShield` (SE-0504), and Swift Build as the default.
- https://developer.apple.com/documentation/swiftui/view/task(name:priority:file:line:_:).md says SwiftUI cancels the `.task` modifier after the view disappears.
- https://developer.apple.com/documentation/swift/task.md says an unstructured `Task` keeps running if you drop the handle, and cancellation is cooperative.
