# Flutter sources

Fetched 12 November 2026.

- https://flutter.dev/blog/whats-new-in-flutter-3-50 announces Flutter 3.50 on 11 November 2026, with Dart 3.14, stable direct native interop, and standalone `material_ui` / `cupertino_ui` as the default for new projects.
- https://docs.flutter.dev/release/release-notes lists 3.50.0 as the current stable notes and keeps 3.47.0 as the previous stable. Do not bump a 3.47 app unless the task asks.
- https://docs.flutter.dev/release/breaking-changes/buttons documents the replacement of `RaisedButton`.
- https://api.flutter.dev/flutter/widgets/BuildContext/mounted.html documents `BuildContext.mounted`. Check it after an `await` before using the context.
