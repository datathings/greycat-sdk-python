const greycat = await gc.sdk.init({ url: URL.parse("http://localhost:5000") });

// Constants
const defaultFile = "tiny";

// Elements
const layout = document.getElementById("layout");
const guiTable = document.createElement("gui-table");
const getCsv = (file) => greycat.call("project::get_csv", [`data/${file}.csv`]).then((table) => guiTable.value = table)

const select = document.createElement("select");
for (let file of ["huge", "tiny"]) {
    const option = document.createElement("option");
    option.innerText = file;
    if (defaultFile === file) {
        option.selected = true;
    }
    select.appendChild(option);
}
select.onchange = (event) => getCsv(event.target.value)

// Render
await getCsv(defaultFile);
layout.replaceChildren(select, guiTable);

export { };
