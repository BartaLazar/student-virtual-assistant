<template>
    <div class="calendar">
        <NavBar2/>
        <div class="uperdiv">
            <p class="cours">Calendrier</p> 
            <div class="uibuttons big">
                <button class="uibutton toggle" @click="toggle" :class="[showSemaine ? 'active': '']">Semaine</button>
                <button class="uibutton toggle" @click="toggle" :class="[showSemaine ? 'active': '']">Jour</button>
            </div>
            <div class="switches-container">
                <input type="radio" id="switchSemaine" name="switchPlan" value="Semaine" checked="checked" />
                <input type="radio" id="switchJour" name="switchPlan" value="Jour" />
                <label  for="switchSemaine">Semaine</label>
                <label for="switchJour">Jour</label>
                <div class="switch-wrapper">
                <div class="switch">
                    <div>Semaine</div>
                    <div>Jour</div>
                </div>
                </div>
            </div>
        </div>
        <div class="actionscal2">
            <p style="color:black;">{{currentDate()}}</p>
            <!--ici le bouton wui bouge entre les jour-->
            <div class="buttonsadd">
                <router-link to="/event" tag="button"><button class="addeven" @click="submit">Ajouter un événement</button></router-link>
                <router-link to="/task" tag="button"><button class="addtask" @click="submit">Ajouter une tâche</button></router-link>
            </div>
        </div>
        <div class="taskliste">
            <p>Tâches</p>
            <ToggleButton/>
        </div>
        
    </div>
  
  </template>
  
  <script>
  // @ is an alias to /src
  import ToggleButton from '@/components/ToggleButton.vue';
  import NavBar2 from '@/components/NavBar2.vue'
  export default {
    name: 'DayView',
    components: {
      NavBar2,
      ToggleButton,
    },
    created() {
        document.body.style.backgroundColor = "#FFFFFF";
    },
    data() {
        return {
            showSemaine: true, 

        };
    },
    methods: {
        toggle() {
            this.showSemaine = !this.showSemaine;
        },
       
        
    },
    methods:{
        currentDate() {
            const current = new Date();
            const date = `${current.getDate()}/${current.getMonth()+1}/${current.getFullYear()}`;
            console.log(this.date);
            return date;
            
        },
        
    }
    
   

  }
  </script>
  <style>
   
    body, html {
        padding: 0;
        margin: 0;
        width: 100%;
        min-height: 100vh;
    }
    .uperdiv{
        height:38px ;
        width:100%;
        background-color:lightgray;
    }
    .cours{
        color:#d80669;
        font-size:25px;
        margin:auto;
        float:left;
        margin-left:13px;
    }
    .actionscal2{
        background-color:rgb(187, 44, 51);
        height: 20%;
        width:100%;
        overflow: scroll;
    }
    
    .buttonsadd{
        float:right;
        
    }
    .addeven{
        background-color:lightgray;
        border-radius: 3px;
        border:0.5px solid ;
        height: 30px;
        width: 180px;
        margin:15px;
    }
    .addtask{
        background-color:lightgray;
        border-radius: 3px;
        border:0.5px solid ;
        height: 30px;
        width: 180px;
    }
    
    .ui{
        border:solid 1px black;
        border-radius: 5px;
    }
    
    :root {
    --switches-bg-color: lightgray;
    --switches-label-color: white ;
    --switch-bg-color: white;
    --switch-text-color: #d80669; 
    }
    .on1{
        color:#d80669;
        background:white;
    }
    .on2{
        color:#d80669;
        background:white;
    }
    .taskliste{
        background-color: #d80669;
        width:35%;
        height: 100vh;
        float: right;

    }



/* resize font-size on html and body level. html is required for widths based on rem */
    @media screen and (min-width: 1024px) {

    
}

@media screen and (max-width: 1024px) {

    html,
    body {
        font-size: 16px;
    }
}

@media screen and (max-width: 600px) {

    html,
    body {
        font-size: 12px;
    }
}

/* a container - decorative, not required */

/* p - decorative, not required */
p {
  margin-top:2rem;
  font-size:0.75rem;
  text-align:center;
}

/* container for all of the switch elements 
    - adjust "width" to fit the content accordingly 
*/


.switches-container {
    border: 1px solid white;
    width: 15rem;
    position: relative;
    padding: 1px;
    position: relative;
    background: var(--switches-bg-color);
    line-height: 2rem;
    border-radius: 5px;
    margin-left: auto;
    margin-right: auto;
   
}

/* input (radio) for toggling. hidden - use labels for clicking on */
.switches-container input {
    visibility: hidden;
    position: absolute;
    top: 0;
}

/* labels for the input (radio) boxes - something to click on */
.switches-container label {
    width: 50%;
    padding: 0;
    margin: 0;
    text-align: center;
    cursor: pointer;
    color: var(--switches-label-color);
}

/* switch highlighters wrapper (sliding left / right) 
    - need wrapper to enable the even margins around the highlight box
*/
.switch-wrapper {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 50%;
    padding: 0.15rem;
    z-index: 3;
    transition: transform .5s cubic-bezier(.77, 0, .175, 1);
    /* transition: transform 1s; */
}

/* switch box highlighter */
.switch {
    border-radius:5px;
    /*border-radius: 3rem;*/
    background: var(--switch-bg-color);
    height: 100%;
}

/* switch box labels
    - default setup
    - toggle afterwards based on radio:checked status 
*/
.switch div {
    width: 100%;
    text-align: center;
    opacity: 0;
    display: block;
    color: var(--switch-text-color) ;
    transition: opacity .2s cubic-bezier(.77, 0, .175, 1) .125s;
    will-change: opacity;
    position: absolute;
    top: 0;
    left: 0;
}

/* slide the switch box from right to left */
.switches-container input:nth-of-type(1):checked~.switch-wrapper {
    transform: translateX(0%);
}

/* slide the switch box from left to right */
.switches-container input:nth-of-type(2):checked~.switch-wrapper {
    transform: translateX(100%);
}

/* toggle the switch box labels - first checkbox:checked - show first switch div */
.switches-container input:nth-of-type(1):checked~.switch-wrapper .switch div:nth-of-type(1) {
    opacity: 1;
}

/* toggle the switch box labels - second checkbox:checked - show second switch div */
.switches-container input:nth-of-type(2):checked~.switch-wrapper .switch div:nth-of-type(2) {
    opacity: 1;
}


  </style>
  