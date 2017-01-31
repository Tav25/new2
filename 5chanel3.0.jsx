////////////////////////////////////////////////////////////////

function myFunc(theObject, t) 
{
   theObject.scale.setValue([101, 101]);
   theObject.stretch = 100;
   //theObject.property("Effects").addProperty("Auto Color"); 
   theObject.startTime=t;
 };


function getRandomArbitary(min, max)
{
  return Math.random() * (max - min) + min;
}


var comp1 = [];// пустой массв для _mp_S_1_rend

var path1 = "../ish/index.mp4";// оспова ролика первый файл путь к нему
var io1 = new ImportOptions(File(path1));
var x1 = app.project.importFile(io1); // index.mp4 загружаем ролик 
var durationIndex = app.project.item(1).duration;
////////////////////////////////////////////////////////////
for (var i = 1; i <= 7; i++) {//цикл повторяется 7, по количеству логотипов и каналов
    var durationRol = getRandomArbitary(610, 630);
    comp1[i] = app.project.items.addComp('_mp_S_'+i+'_rend', 1920, 1080, 1, durationRol, 30);  // создаем _mp_S_1_rend так будет называться файл на выхоле после рендинга
   
    var path2 = "../logo/logo_"+i+".psd"; // путь к файлу с логотипом
    var io2 = new ImportOptions(File(path2));
    var x2 = app.project.importFile(io2);//.логотип загружаем
    
    var rand_mp4 = Math.round(getRandomArbitary(1, 37));
    var path3 = "../ish/ish_"+rand_mp4+".mp4"; // путь к файлу 2 изменить на рандом
    var io3 = new ImportOptions(File(path3));
    var x3 = app.project.importFile(io3);//.загружаем mp4 второй
    
    var rand_mp5 = Math.round(getRandomArbitary(1, 37));
    var path5 = "../ish/ish_"+rand_mp5+".mp4"; // путь к файлу 3 изменить на рандом
    var io5 = new ImportOptions(File(path5));
    var x5 = app.project.importFile(io5);//.загружаем mp4 третий
    
    var rand_mp3 = Math.round(getRandomArbitary(1, 9));
    var path4 = "../sound/"+rand_mp3+".mp3"; // путь к файлу 2
    var io4 = new ImportOptions(File(path4));
    var x4 = app.project.importFile(io4);//.загружаем mp4 второй
    
    comp1[i].layers.add(x4); 
    var durationAll = (x1.duration+x3.duration-11);
    if (durationRol-durationAll > 0) {
        comp1[i].layers.add(x5);
        myFunc(app.project.item(i).layer(2), durationAll-5);
        //break;
    };
        
    comp1[i].layers.add(x3);
    comp1[i].layers.add(x1); //в группу вставяем видео в обратном порядке, после станет нижним слоем
    comp1[i].layers.add(x2);// затем ваставляем логотип 
    
    myFunc(app.project.item(i).layer(2), -6);
    myFunc(app.project.item(i).layer(3), durationIndex-11);
    

    app.project.renderQueue.items.add(comp1[i]);// отправляем очередь рендинга
    
    var f = new File("copy.aep");// сохраняем все изменения
    app.project.save(f);

}
alert("gotovo")
//~     app.project.item(3).layer(2).scale.setValue([101, 101]);
//~     app.project.item(3).layer(2).stretch = 101;
//~     app.project.item(3).layer(2).startTime=-5







