/** @param {{tool?: string, category: string, slug: string}} preset */
export function presetId({ tool, category, slug }) {
    return `${tool ?? "copilot"}-${category}-${slug}`;
}

/** @param {{tool?: string, category: string, technology?: string, slug: string}} preset */
export function presetPath({ tool, category, technology, slug }) {
    return `/${tool ?? "copilot"}/${category}/${technology || "miscellaneous"}/${slug}`;
}

/** @param {string} detail */
export function catalogPaths(detail) {
    const [, tool, category, tech] = detail.split("/");
    return [`/${tool}`, `/${tool}/${category}`, `/${tool}/${category}/${tech}`, detail];
}
