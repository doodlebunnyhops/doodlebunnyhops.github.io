import { defineStackbitConfig, SiteMapEntry, getLocalizedFieldForLocale } from "@stackbit/types";
import { GitContentSource } from "@stackbit/cms-git";
import { getFilePathFromSlugContext } from "@stackbit/cms-git/dist/content-converter";

export default defineStackbitConfig({
  useESM: true,
  stackbitVersion: '~0.6.0',
  devCommand: 'hugo server -b http://localhost:3000/ --port 3000 --disableFastRender --ignoreCache --noHTTPCache --gc --minify',  
  
  contentSources: [
    new GitContentSource({
      rootPath: __dirname,
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
              required: true,
            },
          ],
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
            { name: "noindex", type: "boolean", label: "No Index", const: false,hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false,
            },
          ],
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
            { name: "noindex", type: "boolean", label: "No Index", const: false,hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false,
            },
          ],
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
            { name: "noindex", type: "boolean", label: "No Index", const: false,hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false,
            },
          ],
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
            { name: "noindex", type: "boolean", label: "No Index", const: false,hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false,
            },
          ],
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
            { name: "noindex", type: "boolean", label: "No Index", const: false,hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false,
            },
          ],
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
            { name: "noindex", type: "boolean", label: "No Index", const: false,hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false,
            },
          ],
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
            { name: "noindex", type: "boolean", label: "No Index", const: false,hidden: true },
            { name: "weight", type: "number", label: "Weight", required: false },
            { name: "description", type: "string", label: "Description", required: true },
            {
              name: "images",
              type: "list",
              label: "Images",
              items: { type: "image" },
              required: false,
            },
          ],
        },
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
    // 1. Filter all page models
    const pageModels = models.filter((m) => m.type === "page")

    return documents
      // 2. Filter all documents which are of a page model
      .filter((d) => pageModels.some(m => m.name === d.modelName))
      // 3. Map each document to a SiteMapEntry
      .map((document) => {
        // Map the model name to its corresponding URL
        const urlModel = (() => {
            switch (document.modelName) {
                case 'Page':
                    return 'otherPage';
                case 'Quest':
                  // console.log("Quests ID: ", document.id);
                    return 'lore/quests';
                case 'Casebook':
                    // console.log("Casebook ID: ", document.id);
                    return 'casebook';
                case 'Blog':
                    return 'otherBlog';
                default:
                    return null;
            }
        })();

        // console.log(urlModel);
        // if (!urlModel) return null;
  
        // Use document.slug or fallback to document.id
        // const slug = document.fields.slug || document.id;
        // const frmtSlug = document.fields.slug || document.id.replace(/^.*[\\/](.+)\.md$/, "$1");
        // const frmtSlug = document.fields.slug || 
        //   (document.id.endsWith("_index.md") || document.id.endsWith("__index.md") 
        //       ? "" // Treat as section index, so slug is empty
        //       : document.id.replace(/^.*[\\/](.+)\.md$/, "$1")
        //   );
        
        const frmtSlug = document.id
        .replace(/\\/g, '/') // Normalize backslashes to forward slashes
        .replace(
          /^content[\\/](.+?)[\\/](.+)\.md$/,
          (_, folderPath, fileName) => {
            if (fileName === "_index") {
              // If it's __index.md, return the folder path only
              return `/${folderPath}`;
            } else {
              // Otherwise, return the full path including the file name
              return `/${folderPath}/${fileName}`;
            }
          }
        );

        // console.log("Document ID: ", document.id);
        // console.log("Formated Slug: ", frmtSlug);

        return {
          stableId: document.id,
          urlPath: `${frmtSlug}`,
          // urlPath: `/${document.fields.urlPath}`,
          document,
          isHomePage: false,
        };
      })
      .filter(Boolean) as SiteMapEntry[];
  }
});
