const greycat = await gc.sdk.init({ url: URL.parse("http://localhost:5000") });

// Constants
const defaultFile = "tiny";

// Elements
const fileTable = document.getElementById("file-table");
const fileSelect = document.getElementById("file-select");

const getCsv = (file) => greycat.call("project::get_csv", [`data/${file}.csv`]).then((table) => fileTable.value = table)

for (let file of ["huge", "tiny"]) {
    const option = document.createElement("option");
    option.innerText = file;
    if (defaultFile === file) {
        option.selected = true;
    }
    fileSelect.appendChild(option);
}
fileSelect.onchange = (event) => getCsv(event.target.value)

// Render
await getCsv(defaultFile);

export { };
