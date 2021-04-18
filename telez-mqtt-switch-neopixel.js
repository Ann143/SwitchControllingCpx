
var broker = 'wss://test.mosquitto.org:8081/mqtt';
var client  = mqtt.connect(broker);

var status_header = document.getElementById('status-header')

client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker; 
    console.log('Connected to '+broker)
})
// this is for switch 1
var pub_switch = document.getElementById('pub-switch');
pub_switch.onclick = () => {
    console.log(pub_switch.checked)
    client.publish('cpx-switch/one', String(pub_switch.checked))
}
// this is for switch 2
var pub_switch1 = document.getElementById('pub-switch1');
pub_switch1.onclick = () => {
    console.log(pub_switch1.checked)
    client.publish('cpx-switch/two', String(pub_switch1.checked))
}

// this for the switch 3
var pub_switch2 = document.getElementById('pub-switch2');
pub_switch2.onclick = () => {
    console.log(pub_switch2.checked)
    client.publish('cpx-switch/three', String(pub_switch2.checked))
}
