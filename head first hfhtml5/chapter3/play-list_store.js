/**
 * Created by Administrator on 2016/9/25 0025.
 */
function save(item) {
    var playlistArray = getStoreArray("playlist");
    playlistArray.setItem("playlist",JSON.stringify(playlistArray));

}

function loadPlaylist() {
    var playlistArray = getSavedSongs();
    var ul = document.getElementById("playlist");
    if (playlistArray != null) {
        for(var i = 0; i < playlistArray.length; i++){
            var li = document.createElement("li");
            li.innerHTML = playlistArray[i];
            ul.appendChild(li);
        }
    }
}

function getSaveSongs() {
    return getStoreArray("playlist");
}

function getStoreArray() {
    var playlistArray = localStorage.getItem(key);
    if(playlistArray == null || playlistArray == ""){
        playlistArray = new  Array();

    } else {
        playlistArray = JSON.parse(playlistArray);
    }
    return playlistArray;
}
