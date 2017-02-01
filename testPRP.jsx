"#target premierepro";
alert(app.project.name);
alert (app.project.rootItem.children.numItems)
//app.project.createNewSequence('555', '001','65455');
var activeSequence = app.project.activeSequence;
alert(activeSequence.name)

var arr = []
arr[0] = "d:/1.mp4"
arr[1] = "d:/1a.mp4"
app.project.importFiles(arr);

alert (app.project.rootItem.children[1])