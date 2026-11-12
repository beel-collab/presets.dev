# Rails sources

Fetched 12 November 2026.

- https://rubyonrails.org/2025/10/22/rails-8-1 describes Active Job continuations as resume-from-last-step, not as an idempotency key. The same post covers structured events and local CI.
- Passing an Active Record object to a job uses GlobalID, which stores the class and id. See https://guides.rubyonrails.org/active_job_basics.html
