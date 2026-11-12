# Angular sources

Fetched 12 November 2026.

- Registry: https://registry.npmjs.org/@angular/core reports `latest` 22.2.6. `next` is 22.3.0-rc.0, which is not the line these presets target.
- https://angular.dev/guide/components/advanced-configuration documents OnPush as the default change-detection strategy and `Eager` as the old Default.
- https://angular.dev/guide/di/creating-and-using-services documents `@Service()` with `inject()`. Constructor injection stays on `@Injectable`.
- https://angular.dev/guide/forms/signals/overview is the stable Signal Forms guide.
- https://angular.dev/guide/templates/control-flow documents `@if`, `@for`, and `@switch`. That is the template syntax to generate.
- https://angular.dev/ai/mcp is the Angular CLI MCP server (`npx @angular/cli mcp`).
- https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301 deprecates `*ngIf`, `*ngFor`, and `*ngSwitch` in favor of `@if`, `@for`, and `@switch`. https://angular.dev/api/common/NgIf repeats that deprecation. https://blog.angular.dev/angular-v13-is-now-available-cce66f7bc296 says `ViewContainerRef.createComponent` no longer needs `ComponentFactoryResolver`. The Angular 22 event page does not list that class as removed.
