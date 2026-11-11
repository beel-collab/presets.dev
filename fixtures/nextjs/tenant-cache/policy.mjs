// Decision table for the Next.js tenant-cache presets.
// This module does not import Next.js. It checks the policy the presets describe.

export function securityStatus(version) {
  const match = /^(\d+)\.(\d+)\.(\d+)$/.exec(String(version).trim())
  if (!match) return { status: "unparsed", floor: "16.4.5" }
  const major = Number(match[1])
  const minor = Number(match[2])
  const patch = Number(match[3])
  if (major === 16) {
    if (minor < 4 || (minor === 4 && patch < 5)) {
      return { status: "below-security-floor", floor: "16.4.5" }
    }
    if (minor === 4 && (patch === 5 || patch === 6)) {
      return { status: "patched", floor: "16.4.5" }
    }
    return { status: "above-reviewed", floor: "16.4.6" }
  }
  if (major === 15 && minor === 5) {
    if (patch < 29) return { status: "below-security-floor", floor: "15.5.29" }
    if (patch === 29) return { status: "patched", floor: "15.5.29" }
    return { status: "above-reviewed", floor: "15.5.29" }
  }
  return { status: "version-not-covered", floor: null }
}

export function reviewAction(action) {
  const findings = []
  if (!action.checksSession) {
    findings.push({ id: "unauthenticated-action", severity: "high" })
  }
  if (action.writesClientTenant) {
    findings.push({ id: "client-tenant", severity: "high" })
  }
  if (!action.validatesBody) {
    findings.push({ id: "unvalidated-input", severity: "medium" })
  }
  return findings
}

export function reviewCache(entry) {
  const findings = []
  if (entry.tenantScopedData && !entry.tagIncludesTenant) {
    findings.push({ id: "shared-tenant-tag", severity: "high" })
  }
  if (entry.readsCookiesInside) {
    findings.push({ id: "request-api-in-cache", severity: "high" })
  }
  if (entry.alsoWrappedInUnstableCache) {
    findings.push({ id: "mixed-unstable-cache", severity: "high" })
  }
  if (entry.binaryIdentity) {
    findings.push({ id: "binary-cache-identity", severity: "high" })
  }
  if (entry.privateUserPayload && entry.directive === "use cache") {
    findings.push({ id: "shared-private-payload", severity: "high" })
  }
  return findings
}
