# SwiftUI sources

Fetched 12 November 2026.

- https://www.swift.org/blog/swift-6.4-released/ (15 September 2026) documents async `defer` (SE-0493), `withTaskCancellationShield` (SE-0504), and Swift Build as the default.
- https://developer.apple.com/documentation/swiftui/view/task(name:priority:file:line:_:).md says SwiftUI cancels the `.task` modifier after the view disappears.
- https://developer.apple.com/documentation/swift/task.md says an unstructured `Task` keeps running if you drop the handle, and cancellation is cooperative.
- https://developer.apple.com/forums/thread/760116 says `NavigationView` is deprecated and to use `NavigationStack`. https://developer.apple.com/documentation/swiftui/navigationstack.md is the replacement. https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:).md lists the single-parameter `onChange` only through iOS 17. https://developer.apple.com/documentation/swiftui/view/onchange(of:initial:_:).md is the current method. https://developer.apple.com/documentation/swiftui/view/foregroundcolor(_:).md does not mark `foregroundColor` deprecated.
