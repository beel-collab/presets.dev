import assert from "node:assert/strict"
import { test } from "node:test"

import { reviewAction, reviewCache, securityStatus } from "./policy.mjs"

test("16.4.5 and 16.4.6 are the reviewed patched builds", () => {
  assert.equal(securityStatus("16.4.5").status, "patched")
  assert.equal(securityStatus("16.4.6").status, "patched")
})

test("16.4.4 and earlier 16.x stay below the security floor", () => {
  assert.equal(securityStatus("16.4.4").status, "below-security-floor")
  assert.equal(securityStatus("16.3.9").status, "below-security-floor")
  assert.equal(securityStatus("16.2.0").status, "below-security-floor")
})

test("a later 16 than 16.4.6 is above the reviewed build", () => {
  assert.equal(securityStatus("16.4.7").status, "above-reviewed")
  assert.equal(securityStatus("16.5.0").status, "above-reviewed")
})

test("15.5.29 is patched and its neighbors are not treated as the same review", () => {
  assert.equal(securityStatus("15.5.28").status, "below-security-floor")
  assert.equal(securityStatus("15.5.29").status, "patched")
  assert.equal(securityStatus("15.5.30").status, "above-reviewed")
  assert.equal(securityStatus("15.4.1").status, "version-not-covered")
  assert.equal(securityStatus("14.2.15").status, "version-not-covered")
})

test("prerelease and workspace specifiers are unparsed", () => {
  assert.equal(securityStatus("16.4.6-canary.1").status, "unparsed")
  assert.equal(securityStatus("workspace:*").status, "unparsed")
})

test("a signed-out write that trusts the client tenant is high", () => {
  const ids = reviewAction({
    checksSession: false,
    writesClientTenant: true,
    validatesBody: false,
  }).map((item) => item.id)
  assert.deepEqual(ids, ["unauthenticated-action", "client-tenant", "unvalidated-input"])
})

test("a session-scoped validated write has no action findings", () => {
  assert.deepEqual(
    reviewAction({
      checksSession: true,
      writesClientTenant: false,
      validatesBody: true,
    }),
    [],
  )
})

test("tenant rows with a shared notes tag are a high finding", () => {
  const ids = reviewCache({
    tenantScopedData: true,
    tagIncludesTenant: false,
    readsCookiesInside: true,
    alsoWrappedInUnstableCache: true,
    binaryIdentity: true,
    privateUserPayload: true,
    directive: "use cache",
  }).map((item) => item.id)
  assert.deepEqual(ids, [
    "shared-tenant-tag",
    "request-api-in-cache",
    "mixed-unstable-cache",
    "binary-cache-identity",
    "shared-private-payload",
  ])
})

test("public tenant-tagged cache with no request data has no cache findings", () => {
  assert.deepEqual(
    reviewCache({
      tenantScopedData: true,
      tagIncludesTenant: true,
      readsCookiesInside: false,
      alsoWrappedInUnstableCache: false,
      binaryIdentity: false,
      privateUserPayload: false,
      directive: "use cache",
    }),
    [],
  )
})

test("a marketing cache with no tenant data is not a shared-tag finding", () => {
  assert.deepEqual(
    reviewCache({
      tenantScopedData: false,
      tagIncludesTenant: false,
      readsCookiesInside: false,
      alsoWrappedInUnstableCache: false,
      binaryIdentity: false,
      privateUserPayload: false,
      directive: "use cache",
    }),
    [],
  )
})
