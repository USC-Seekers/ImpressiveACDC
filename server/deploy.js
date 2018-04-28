var fs = require('fs');
var path = require('path');
var child_process = require('child_process');

var deleteFolderRecursive = function(path) {
    if( fs.existsSync(path) ) {
        fs.readdirSync(path).forEach(function(file,index){
            var curPath = path + "/" + file;
            if(fs.lstatSync(curPath).isDirectory()) { // recurse
                deleteFolderRecursive(curPath);
            } else { // delete file
                fs.unlinkSync(curPath);
            }
        });
        fs.rmdirSync(path);
    }
};

var deploy = function (pushObj) {
    var name = pushObj["repository"]["name"];
    var git = pushObj["repository"]["clone_url"];

    var repositoryPath = path.join(__dirname, "public", name);
    deleteFolderRecursive(repositoryPath);

    fs.mkdir(repositoryPath);
    child_process.spawn("git", ["clone", git, repositoryPath]);
};


module.exports = deploy;
