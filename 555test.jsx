////////////////////////////////////////////////////////////////
#target afterEffects
var path1 = "./1.mp4"; // путь к файлу, файл находится в папке со скриптом
var file01 = new ImportOptions(File(path1));
var x1 = app.project.importFile(file01); // 1.mp4 загружаем ролик 
var durationRol = getRandomArbitary(610, 630);//длинна ролика в секундах от 610 до 630 секунд
comp1 = app.project.items.addComp('rend01', 1920, 1080, 1, durationRol, 30);// композиция 