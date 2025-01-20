// stackbit.config.ts
import { defineStackbitConfig } from "@stackbit/types";
import { GitContentSource } from "@stackbit/cms-git";
var stackbit_config_default = defineStackbitConfig({
  useESM: true,
  stackbitVersion: "~0.6.0",
  devCommand: "hugo server -b http://localhost:3000/ --port 3000 --disableFastRender --ignoreCache --noHTTPCache --gc --minify",
  contentSources: [
    new GitContentSource({
      rootPath: "C:\\Users\\ashle\\git\\doodlebunnyhops.github.io",
      contentDirs: [
        "content/lore",
        "content/casebook"
      ],
      models: [
        {
          name: "Folder",
          type: "object",
          label: "Folder",
          fields: [
            {
              name: "title",
              type: "string",
              label: "Folder Name",
              required: true
            }
          ]
        },
        {
          name: "Quest",
          type: "page",
          urlPath: "/lore/quests/{slug}",
          filePath: "content/lore/quests/{slug}.md",
          fields: [
            { name: "slug", type: "slug", hidden: true },
            { name: "linktitle", type: "string", label: "Link Title", required: true },
            { name: "title", type: "string", label: "Title", required: true },
            { name: "noindex", type: "boolean", label: "No Index", const: false, hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false
            }
          ]
        },
        {
          name: "special_tools",
          label: "Quests: Special Tools",
          type: "page",
          urlPath: "/lore/special_tools/{slug}",
          filePath: "content/lore/special_tools/{slug}.md",
          fields: [
            { name: "slug", type: "slug", hidden: true },
            { name: "linktitle", type: "string", label: "Link Title", required: true },
            { name: "title", type: "string", label: "Title", required: true },
            { name: "noindex", type: "boolean", label: "No Index", const: false, hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false
            }
          ]
        },
        {
          name: "tools",
          label: "Quests: Tools",
          type: "page",
          urlPath: "/lore/tools/{slug}",
          filePath: "content/lore/tools/{slug}.md",
          fields: [
            { name: "slug", type: "slug", hidden: true },
            { name: "linktitle", type: "string", label: "Link Title", required: true },
            { name: "title", type: "string", label: "Title", required: true },
            { name: "noindex", type: "boolean", label: "No Index", const: false, hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false
            }
          ]
        },
        {
          name: "walkthrough",
          label: "Walkthrough",
          type: "page",
          urlPath: "/lore/{slug}",
          filePath: "content/lore/{slug}.md",
          fields: [
            { name: "slug", type: "slug", hidden: true },
            { name: "linktitle", type: "string", label: "Link Title", required: true },
            { name: "title", type: "string", label: "Title", required: true },
            { name: "noindex", type: "boolean", label: "No Index", const: false, hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false
            }
          ]
        },
        {
          name: "Casebook",
          type: "page",
          urlPath: "/casebook/{slug}",
          filePath: "content/casebook/{slug}.md",
          fields: [
            { name: "slug", type: "slug", hidden: true },
            { name: "linktitle", type: "string", label: "Link Title", required: true },
            { name: "title", type: "string", label: "Title", required: true },
            { name: "noindex", type: "boolean", label: "No Index", const: false, hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false
            }
          ]
        },
        {
          name: "Computer",
          label: "Casebook Computer",
          type: "page",
          groups: ["casebook"],
          urlPath: "/casebook/computer/{slug}",
          filePath: "content/casebook/computer/{slug}.md",
          fields: [
            { name: "slug", type: "slug", hidden: true },
            { name: "linktitle", type: "string", label: "Link Title", required: true },
            { name: "title", type: "string", label: "Title", required: true },
            { name: "noindex", type: "boolean", label: "No Index", const: false, hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false
            }
          ]
        },
        {
          name: "Interesting",
          label: "Casebook Interesting",
          type: "page",
          groups: ["casebook"],
          urlPath: "/casebook/interesting/{slug}",
          filePath: "content/casebook/interesting/{slug}.md",
          fields: [
            { name: "slug", type: "slug", hidden: true },
            { name: "linktitle", type: "string", label: "Link Title", required: true },
            { name: "title", type: "string", label: "Title", required: true },
            { name: "noindex", type: "boolean", label: "No Index", const: false, hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false
            }
          ]
        }
      ],
      assetsConfig: {
        referenceType: "static",
        staticDir: "assets/images",
        uploadDir: "/",
        publicPath: "/images"
      }
    })
  ],
  siteMap: ({ documents, models }) => {
    const pageModels = models.filter((m) => m.type === "page");
    return documents.filter((d) => pageModels.some((m) => m.name === d.modelName)).map((document) => {
      const urlModel = (() => {
        switch (document.modelName) {
          case "Page":
            return "otherPage";
          case "Quest":
            return "lore/quests";
          case "Casebook":
            return "casebook";
          case "Blog":
            return "otherBlog";
          default:
            return null;
        }
      })();
      const frmtSlug = document.id.replace(/\\/g, "/").replace(
        /^content[\\/](.+?)[\\/](.+)\.md$/,
        (_, folderPath, fileName) => {
          if (fileName === "_index") {
            return `/${folderPath}`;
          } else {
            return `/${folderPath}/${fileName}`;
          }
        }
      );
      return {
        stableId: document.id,
        urlPath: `${frmtSlug}`,
        // urlPath: `/${document.fields.urlPath}`,
        document,
        isHomePage: false
      };
    }).filter(Boolean);
  }
});
export {
  stackbit_config_default as default
};
//# sourceMappingURL=stackbit.config.Z7H5HF3L.mjs.map
