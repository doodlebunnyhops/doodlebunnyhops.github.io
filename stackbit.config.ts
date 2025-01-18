import { defineStackbitConfig } from "@stackbit/types";
import { GitContentSource } from "@stackbit/cms-git";


export default defineStackbitConfig({
    stackbitVersion: "~0.6.0",

    contentSources: [
    new GitContentSource({
        assetsConfig: {
          referenceType: "static",
          staticDir: "public",
          uploadDir: "images",
          publicPath: "/"
        },
        rootPath: __dirname,
        contentDirs: [
        "content/about",
        "content/blog",
        "content/casebook",
        "content/contribute",
        "content/lore/quests", // Handles quests specifically
        "content/lore", // Handles other lore content
        "content/special_tools", // Add other directories as needed
        ],
        models: [
        {
            name: "Quest",
            type: "page",
            urlPath: "/quests/{slug}",
            filePath: "content/lore/quests/{slug}.md",
            fields: [
            { name: "title", type: "string", required: true },
            { name: "date", type: "string", required: false },
            { name: "description", type: "string", required: false },
            ],
        },
        {
            name: "BlogPost",
            type: "page",
            urlPath: "/blog/{slug}",
            filePath: "content/blog/{slug}.md",
            fields: [
            { name: "title", type: "string", required: true },
            { name: "author", type: "string", required: false },
            { name: "date", type: "string", required: false },
            ],
        },
        {
            name: "Casebook",
            type: "page",
            urlPath: "/casebook/{slug}",
            filePath: "content/casebook/{slug}.md",
            fields: [
            { name: "title", type: "string", required: true },
            { name: "date", type: "string", required: false },
            ],
        },
        // Add additional models for other content types as needed
        ],
    }),
    ],
});
