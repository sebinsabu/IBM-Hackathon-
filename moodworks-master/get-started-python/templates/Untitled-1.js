<html>

<p id ="smname"></p>

</html>


<script>
var thehours = new Date().getHours();
var themessage;
var morning = ('Good morning');
var afternoon = ('Good afternoon');
var evening = ('Good evening');

  if (thehours >= 0 && thehours < 12) {
    themessage = morning; 

  } else if (thehours >= 12 && thehours < 17) {
    themessage = afternoon;

  } else if (thehours >= 17 && thehours < 24) {
    themessage = evening;
  }

var helloGreeting = ["What's happening","How's it going?","What's up?","Hi!","How are things","What’s new?","It’s good to see you","Howdy!","Hey there.","Yo!","Hey"];
var name = "! Sebin. ";
var greeting = themessage+name+helloGreeting[getRandomInt(helloGreeting.length)];
document.getElementById('smname').innerHTML = greeting;

function getRandomInt(max) 
{
  
  return Math.floor(Math.random() * Math.floor(max));

}

</script>