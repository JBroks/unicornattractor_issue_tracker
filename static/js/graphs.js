/*
d3.queue()
    .defer(d3.json, "{% url 'testData' %}")
    .await(makeGraphs);
    
function makeGraphs(error, data) {
    let ticketData = crossfilter(data);

    // Call functions for each individual chart

   showRecordsCount(ticketData);

    // Render all charts
    dc.renderAll();

}


function showRecordsCount(ticketData) {

    let dim = ticketData;
    let allRecords = ticketData.groupAll();

    dc.dataCount('.dc-data-count')
        .group(allRecords)
        .dimension(dim);
}


d3.json("/testData/", function(error, data) {
    let ticketData = crossfilter(data);

    // Call functions for each individual chart

    showRecordsCount(ticketData);

    // Render all charts
    dc.renderAll();

});*/
/*
function showRecordsCount(ticketData) {

    let dim = ticketData;
    let allRecords = ticketData.groupAll();

    dc.dataCount('.dc-data-count')
        .group(allRecords)
        .dimension(dim);
}


d3.json("{% url 'testData' %}", function(data) {
    console.log(data);
});
*/