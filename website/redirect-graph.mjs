/**
 * @param {Record<string, string>} redirects
 * @param {string} source
 * @param {string} destination
 */
export function redirectTerminal(redirects, source, destination) {
    const visited = new Set([source]);
    while (Object.hasOwn(redirects, destination)) {
        if (visited.has(destination)) throw new Error(`Redirect cycle at ${destination}`);
        visited.add(destination);
        destination = redirects[destination];
    }
    return destination;
}

/** @param {Record<string, string>} redirects */
export function validateRedirectGraph(redirects) {
    if (!redirects || typeof redirects !== "object" || Array.isArray(redirects)) {
        throw new Error("Expected a map of permanent redirects");
    }
    const pairs = Object.entries(redirects);
    for (const [source, destination] of pairs) {
        if (!source.startsWith("/") || source.startsWith("//")) {
            throw new Error(`Expected a local redirect source, got ${JSON.stringify(source)}`);
        }
        if (typeof destination !== "string" || !destination.startsWith("/") || destination.startsWith("//")) {
            throw new Error(`Expected a local redirect destination, got ${JSON.stringify(destination)}`);
        }
    }
    for (const [source, destination] of pairs) redirectTerminal(redirects, source, destination);
}
