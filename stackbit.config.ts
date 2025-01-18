import { defineStackbitConfig, SiteMapEntry } from "@stackbit/types";
import { GitContentSource } from "@stackbit/cms-git";

export default defineStackbitConfig({
  contentSources: [
    new GitContentSource({
      rootPath: __dirname,
      contentDirs: [
        "content/about",
        "content/blog",
        "content/casebook",
        "content/contribute",
        "content/lore/quests",
        "content/lore"
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
            { name: "description", type: "string", required: false }
          ]
        },
        {
          name: "BlogPost",
          type: "page",
          urlPath: "/blog/{slug}",
          filePath: "content/blog/{slug}.md",
          fields: [
            { name: "title", type: "string", required: true },
            { name: "author", type: "string", required: false },
            { name: "date", type: "string", required: false }
          ]
        },
        {
          name: "Casebook",
          type: "page",
          urlPath: "/casebook/{slug}",
          filePath: "content/casebook/{slug}.md",
          fields: [
            { name: "title", type: "string", required: true },
            { name: "date", type: "string", required: false }
          ]
        }
      ]
    })
  ],
  siteMap: ({ documents, models }) => {
    const pageModels = models.filter((m) => m.type === "page");

    return documents
      .filter((d) => pageModels.some((m) => m.name === d.modelName))
      .map((document) => {
        let urlPath;

        switch (document.modelName) {
          case "Quest":
            urlPath = `/quests/${document.slug}`;
            break;
          case "BlogPost":
            urlPath = `/blog/${document.slug}`;
            break;
          case "Casebook":
            urlPath = `/casebook/${document.slug}`;
            break;
          default:
            return null;
        }

        return {
          stableId: document.id,
          urlPath,
          document,
          isHomePage: false
        };
      })
      .filter(Boolean) as SiteMapEntry[];
  }
});
