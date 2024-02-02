const URI = "https://swapi-api.hbtn.io/api/people/5/?format=json";


async function getName() {
    const result = await fetch(URI);
    return result.json();
}
getName()
    .then((result) => {
        console.log("result---", result.name);
    });
