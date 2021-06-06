//BUTTONS
const buttonvisual = document.querySelector("#vbutton");
const buttonplan = document.querySelector("#pbutton");
const buttonstats = document.querySelector("#sbutton");

let onpage = buttonvisual

//PAGES
const visualize = document.querySelector("#one");
const plan = document.querySelector("#two");
const stats = document.querySelector("#three");

const setup = () => {
    console.log("Staring Up!")
    visualize.classList.remove("hide");
    plan.classList.add("hide");
    stats.classList.add("hide");
    buttonvisual.classList.add("selected")
}

const changeLabels = (button) => {
    onpage.classList.remove("selected");
    button.classList.add("selected");
    onpage = button;
}

buttonvisual.addEventListener("click", (e) => {

    visualize.classList.remove("hide");
    plan.classList.add("hide");
    stats.classList.add("hide");
    changeLabels(buttonvisual);
});

buttonplan.addEventListener("click", (e) => {

 
    plan.classList.remove("hide");
    visualize.classList.add("hide");
    stats.classList.add("hide");
    changeLabels(buttonplan);
});

buttonstats.addEventListener("click", (e) => {


    stats.classList.remove("hide");
    visualize.classList.add("hide");
    plan.classList.add("hide");
    changeLabels(buttonstats);
})







//DO THE CHARTS
let species = []

const data1 = {
    labels: ["One", "Two", "Three", "Four", "Five", "Six", "Seven"],

    datasets: [
        {
            label: species[0],
            data: [{"age": 232, "volume": 11309}, {"age": 174, "volume": 9952}, {"age": 263, "volume": 16625}, {"age": 280, "volume": 17520}, {"age": 160, "volume": 14162}],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgb(255, 99, 132)',
        },
        {
            label: 'Dataset 2',
            data: [35, 20, 25, 11, 14, 9, 6],
            borderColor: 'rgb(104, 237, 108)',
            backgroundColor: 'rgb(0, 153, 161)',
        }
    ]
};

const configscatter = {
    type: 'scatter',
    data: data1,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Age vs Volume Scatter Chart'
            }
            
        },
        parsing: {
            xAxisKey: 'age',
            yAxisKey: 'volume'
        },

    },
};

const setCharts = () =>{
    data1.datasets[0].label = species[0];

}

const getspecies = fetch("http://127.0.0.1:8000/species").then((response) => {return response.json()}).then((data) => {

    for(let i = 0; i < data.length; i++){
        species[i] = data[i][i+1];
    }
    console.log("SPECIES ARE" + species[0]);
});







//API CALLS
const apitest = (data) => {
    console.log(data);
    console.log(data[0]);
    console.log(data[0].height);
}

const getGraph = (graphnumber, specie) =>{
    let url = "http://127.0.0.1:8000/graph" + graphnumber + "/" + specie;
    fetch(url).then((response) => {console.log(response); return response.json()}).then((data) => {apitest(data);});
}

// getGraph(2,1);













var myChart = new Chart(document.querySelector('#myChart'),configscatter);



