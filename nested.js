import fs from "fs";
import path from "path";

function getNestedCasebookModels(basePath) {
  const directories = [];

  function scanDir(currentPath, parentModel) {
    const items = fs.readdirSync(currentPath, { withFileTypes: true });
    items.forEach((item) => {
      const fullPath = path.join(currentPath, item.name);
      if (item.isDirectory()) {
        const modelName = `Casebook_${item.name.replace(/-/g, "_")}`;
        directories.push({
          name: modelName,
          parent: parentModel,
          folder: fullPath.replace(basePath, ""),
        });
        scanDir(fullPath, modelName); // Recursively scan subdirectories
      }
    });
  }

  scanDir(basePath, null);
  return directories;
}

const casebookBasePath = path.join(__dirname, "content/casebook");
const casebookFolders = getNestedCasebookModels(casebookBasePath);

const casebookModels = casebookFolders.map((folder) => ({
  name: folder.name,
  type: "page",
  label: `Casebook: ${folder.folder.replace("/", " > ")}`, // Friendly name in the editor
  urlPath: `/casebook${folder.folder}/{slug}`,
  filePath: `content/casebook${folder.folder}/{slug}.md`,
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
      required: false,
    },
  ],
}));
