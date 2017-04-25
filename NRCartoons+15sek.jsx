////////////////////////////////////////////////////////////////
#target afterEffects

function myFunc(theObject, t) 
{
   theObject.scale.setValue([101, 101]);
   theObject.stretch = 100;
   theObject.startTime=t;
 };


function getRandomArbitary(min, max)
{
  return Math.random() * (max - min) + min;
}


var comp1 = [];// пустой массв для _mp_S_1_rend

var kolfile_mp4=41;

   

////////////////////////////////////////////////////////////
for (var i = 1; i <=5; i++) {//<=5 цикл повторяется 7, по количеству логотипов и каналов
    
	var rand_mp4 = Math.round(getRandomArbitary(1, kolfile_mp4))
    
    var path1 = "./ish/ish_"+rand_mp4+".mp4"; // путь к файлу 1 изменить на рандом
    //var path1 = "./ish/index.mp4";// основа ролика первый файл путь к нему
    var io1 = new ImportOptions(File(path1));
    var x1 = app.project.importFile(io1); // index.mp4 загружаем ролик 
    //var durationIndex = app.project.item(1).duration/2;  
    
    
    var durationRol = getRandomArbitary(610, 630);
    comp1[i] = app.project.items.addComp('_NRS_S_'+i+'_rend', 1920, 1080, 1, durationRol, 30);  // создаем _mp_S_1_rend так будет называться файл на выхоле после рендинга
   
    var path2 = "./logo/logo_3.psd"; // путь к файлу с логотипом Мульт парада
    var io2 = new ImportOptions(File(path2));
    var x2 = app.project.importFile(io2);//.логотип загружаем
    
    var rand_mp4 = Math.round(getRandomArbitary(1, kolfile_mp4));
    var path3 = "./ish/ish_"+rand_mp4+".mp4"; // путь к файлу 2 изменить на рандом
    var io3 = new ImportOptions(File(path3));
    var x3 = app.project.importFile(io3);//.загружаем mp4 второй
    
    var rand_mp5 = Math.round(getRandomArbitary(1, 37));
    var path5 = "./ish/ish_"+rand_mp5+".mp4"; // путь к файлу 3 изменить на рандом
    var io5 = new ImportOptions(File(path5));
    var x5 = app.project.importFile(io5);//.загружаем mp4 третий
	
	//
	//var rand_mp5 = Math.round(getRandomArbitary(1, 37));
    var path15s = "./ish/15sek3.mp4"; // путь к файлу 3 изменить на рандом
    var s15 = new ImportOptions(File(path15s));
    var x15 = app.project.importFile(s15);//.загружаем mp4 третий
	//
    
    var rand_mp3 = Math.round(getRandomArbitary(1, 9));
    var path4 = "./sound/"+rand_mp3+".mp3"; // путь к файлу 2
    var io4 = new ImportOptions(File(path4));
    var x4_sound = app.project.importFile(io4);//.загружаем mp4 второй
	
	var nuvvid = "./nuvvid/"+i+".png"; // путь к файлу 
    var nuvvid_io = new ImportOptions(File(nuvvid));
    var x_nuvvid = app.project.importFile(nuvvid_io);// загружаем
    
    comp1[i].layers.add(x4_sound); //l5
	comp1[i].layers.add(x_nuvvid);//счетчик
    comp1[i].layers.add(x5);//3 l4
    comp1[i].layers.add(x3);//2 l3
    comp1[i].layers.add(x1); //1 l2
	comp1[i].layers.add(x15);//3 l4
    comp1[i].layers.add(x2);//logo l1
	
	myFunc(app.project.item(i).layer(2), (app.project.item(i).layer(1).outPoint)-10); //начало ролика 15сек -10секунд от конца
	myFunc(app.project.item(i).layer(6), (app.project.item(i).layer(1).outPoint)-5);
	app.project.item(i).layer(6).scale.setValue([100, 100]);
	
	
    dd=getRandomArbitary(176, 186)
	if (app.project.item(i).layer(3).outPoint < dd){
		alert('жопа1');
	}
	if (app.project.item(i).layer(4).outPoint < dd){
		alert('жопа2');
	}
	if (app.project.item(i).layer(5).outPoint < dd){
		alert('жопа3');
	}
	

	//1й ролик начало -4 конец dd
	myFunc(app.project.item(i).layer(3), -8);	
    app.project.item(i).layer(3).outPoint=dd;//dlinna pervogo rolika
	//2й
    myFunc(app.project.item(i).layer(4), dd-6);
	app.project.item(i).layer(4).outPoint=dd+dd;
	//3й
	myFunc(app.project.item(i).layer(5), app.project.item(i).layer(4).outPoint-6);
	app.project.item(i).layer(5).outPoint=durationRol-9;

    
    
    app.project.item(i).layer(1).outPoint=durationRol;//обрезка по длинне клипа
    app.project.item(i).layer(2).outPoint=durationRol-1;
    app.project.item(i).layer(6).outPoint=durationRol;
	app.project.item(i).layer(7).outPoint=durationRol;

    app.project.renderQueue.items.add(comp1[i]);// отправляем очередь рендинга
    
	var l = new Date();

	
    var f = new File("arhiv_MP/NRS_"+l.toLocaleDateString()+".aep");// сохраняем все изменения
    app.project.save(f);

}








