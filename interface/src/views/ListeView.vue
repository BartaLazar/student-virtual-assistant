<template>
    <div class="liste">
      <ListeComp/>
      <div class="listcontent">
        <div class="buttonsadd">
          <router-link to="/event" tag="button"><button class="modif" @click="submit">Modifier</button></router-link>
          <router-link to="/event" tag="button"><button class="addeven" @click="submit">Ajouter un événement</button></router-link>
          <router-link to="/task" tag="button"><button class="addtask" @click="submit">Ajouter une tâche</button></router-link>
        </div>
        <div class="box">
          <router-link to="/courses"><radial-progress-bar class="rpb"
          :diameter="200"
          :completed-steps="completedCourses"
          :total-steps="totalCourses"
          :startColor=" startColor"
          :stopColor="stopColor"
          :innerStrokeColor = "innerStrokeColor"	>
          {{ completedCourses }}/{{ totalCourses }}
          <label class="largelabel">Cours</label>
        </radial-progress-bar></router-link>
          
        <router-link to="/experiences">
           <radial-progress-bar class="rpb"
            :diameter="200"
            :completed-steps="completedExps"
            :total-steps="totalExps"
            :startColor=" startColor"
            :stopColor="stopColor"
            :innerStrokeColor = "innerStrokeColor">
            {{ completedExps }}/{{ totalExps }}
            <label class="largelabel">Expérience/TP</label>
          </radial-progress-bar>
        </router-link>
       
       <router-link to="/lectures">
         <radial-progress-bar class="rpb"
          :diameter="200"
          :completed-steps="completedLects"
          :total-steps="totalLects"
          :startColor=" startColor"
          :stopColor="stopColor"
          :innerStrokeColor = "innerStrokeColor">
          {{ completedLects }}/{{ totalLects }}
          <label class="largelabel">Lectures</label>
        </radial-progress-bar>
       </router-link>
       
       <router-link to="/revisions">
         <radial-progress-bar class="rpb"
          :diameter="200"
          :completed-steps="completedRevs"
          :total-steps="totalRevs"
          :startColor=" startColor"
          :stopColor="stopColor"
          :innerStrokeColor = "innerStrokeColor">
          {{ completedRevs }}/{{ totalRevs }}
          <label class="largelabel">Révision</label>
        </radial-progress-bar>
       </router-link>
       
        </div>
        
          <br>
          <hr>
          <br>
          <div>
            <div class="boxes1">
            <div class="div1">
              <h5>Cours</h5>
              <hr class="box">
              <h5 class="thin" id="prof"></h5>
              <h5>Horaire</h5>
              <h5 class="thin">Date</h5>
              <h5 class="thin" >Occurence</h5>
              <h5 class="thin">Salle</h5>
            </div>
            <div class="div2">
              <h5>Séminaire</h5>
              <hr class="box">
              <h5 class="thin">Prof</h5>
              <h5>Horaire</h5>
              <h5 class="thin">Date</h5>
              <h5 class="thin">Occurence</h5>
              <h5 class="thin">Salle</h5>
            </div>
            <div class="div3">
              <h5>Mediaserver </h5>
              <hr class="box">
              <h5 class="thin">Contenu externe </h5>
              <h5 class="thin">link</h5>
            </div>
            
        </div>
        <div class="boxes2">
            <div class="div1">
              <h5>Moodle </h5>
              <hr class="box">
              <h5 class="thin">Contenu externe</h5> 
              <h5 class="thin">link</h5>
            </div>
            <div class="div2">
              <h5>Quizlet </h5>
              <hr class="box">
              <h5 class="thin">Contenu externe</h5> 
              <h5 class="thin">link</h5>
            </div>
            <div class="div3">
              <h5>Discord</h5> 
              <hr class="box">
              <h5 class="thin">Contenu externe</h5> 
              <h5 class="thin">link</h5>
            </div>
        </div>
      </div>    
      </div>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
  import RadialProgressBar from "vue3-radial-progress";
  import ListeComp from '@/components/ListeComp.vue';
  import { method } from 'lodash';
  import {BASE_PATH} from '@/common/common.js';
  import axios from 'axios';
  import NavBar2 from '@/components/NavBar2.vue';
  import { ref, defineComponent } from "vue";
  export default {
    name: 'ListeView',
    components: {
      ListeComp,
      NavBar2,
      RadialProgressBar,
    },
    setup(){
      const completedCourses = ref(5);
      const totalCourses = ref(10);
      const completedExps = ref(3);
      const totalExps = ref(10);
      const completedLects = ref(2);
      const totalLects = ref(5);
      const completedRevs = ref(0);
      const totalRevs = ref(10);
      const startColor = ref('#d80669');
      const stopColor	= ref('#d80669');
      const innerStrokeColor = ref("#e08bb3")
      return {
        completedCourses,
        totalCourses,
        completedExps,
        totalExps,
        completedLects,
        totalLects,
        completedRevs,
        totalRevs,
        startColor,
        stopColor,
        innerStrokeColor
        }
    },
    
    created() {
      document.body.style.backgroundColor = "#FFFFFF";
        const userId = localStorage.getItem("userId");
          
        const courseId = localStorage.getItem("courseId");
            axios.get(`${BASE_PATH}${userId}/course/data?course=${courseId};`)
            .then((response) => {
              if(response.data["status_code"] == 200 || response.data["status_code"] == 201){
                const course_infos = response.data.data; 
                console.log("infos for progress bar",course_infos)        
              }})
              
        // document.body.style.backgroundColor = "#FFFFFF";
        // //const api_url = '{{api}}';
        // const api_url = 'http://127.0.0.1:5000/id=0d3b57d6-7457-4cf9-ac43-5f8760084a2a/course/data?course=f690ef95-fab4-4701-a35f-ebe22d3bbf0e';
        // async function fetchText() {
        //   let response = await fetch(api_url);
        //   let data = await response.json();
        //   const text = data;
        //   console.log(text);
        //   const myArr = text;
        //   console.log(text);
        //   for(let i = 0; i < myArr["courses"].length; i++){
        //     if(myArr["courses"][i]["type"]=="Cours"){
        //       for(let j = 0; j < myArr["courses"][i]["teachers_full_name"].length; j++){
        //         console.log("this",myArr["courses"][i]["teachers_full_name"][j]);
        //                     document.getElementById("prof").innerHTML += myArr["courses"][i]["teachers_full_name"][j];
        //       }
        //     } 
        //   }
          
        // }
        // fetchText();
    },
    data(){
        return{
            selectedcourse: '',
            courses: [],
            item:'',
      
        }
    },
  }
</script>
  <style>
    body, html {
      padding: 0;
      margin: 0;
      width: 100%;
      min-height: 100vh;/*to cover the full page height*/
    }
    
    hr{
      width:70%;
      align-items: center;
      margin:auto;
    }
    .buttonsadd{
      float:right;
      margin-right:100px;
    }
    .modif{
      background-color:#d80669;
      border-radius: 3px;
      border:0.5px solid ;
      height: 30px;
      width: 180px;
      margin:15px;
      margin-right:5px;
      color:white;
    }
    .addeven{
        background-color:#d80669;
        border-radius: 3px;
        border:0.5px solid ;
        height: 30px;
        width: 180px;
        margin:15px;
        color:white;
        
    }
    .addtask{
        background-color:#d80669;
        border-radius: 3px;
        border:0.5px solid ;
        height: 30px;
        width: 180px;
        color:white;
    }
    .listcontent{
      position: relative;
    }
    .box{
      display: flex;
      align-content:center;
      justify-content: center;
      border-radius: 4px;
      margin:auto;
      width:80%;
     
    }
    .rpb{
      margin-right: 90px;
    }
    .boxes1{
      display: flex;
      align-content:center;
      justify-content: center;
      border-radius: 4px;
      margin:auto;
      width:70%;
  
    }
    h5{
      font-size:14px;
      font-family: Arial, Helvetica, sans-serif;
      font-family: 'Courier New', Courier, monospace, sans-serif;
      font-weight: bold;
    }
    .thin{
      font-size:13px;
      font-family: 'Courier New', Courier, monospace, sans-serif;
      font-weight: normal;
    }
    .boxes1 div{
      padding:15px;
      align-items:center;
      background-color:#e08bb3;
      width:100%;
      height:160px;
      margin: 10px;
      border: black solid 0.5px ;
      border-radius: 4px;
    }
    .boxes2{
      display: flex;
      align-content:center;
      justify-content: center;
      
      border-radius: 4px;
      margin:auto;
      width:70%;
    }
    .boxes2 div{
      padding:10px;
      padding-left:15px;
      align-items:center;
      background-color:#e08bb3;
      width:100%;
      height:160px;
      margin: 10px;
      border: black solid 0.5px ;
      border-radius: 4px;
    }
    * {
    margin: 0;
    padding: 0;
    font-family: 'Lato', sans-serif;
}

.progress {
    position: absolute;   
    height: 160px;
    width: 160px;
    cursor: pointer;
    top: 50%;
    left: 50%;
    margin: -80px 0 0 -80px;
}

.progress-circle {
  transform: rotate(-90deg);
	margin-top: -40px;
}

.progress-circle-back {
	fill: none; 
	stroke: #D2D2D2;
	stroke-width:10px;
}

.progress-circle-prog {
	fill: none; 
	stroke: #7E3451;
	stroke-width: 10px;  
	stroke-dasharray: 0 999;    
	stroke-dashoffset: 0px;
    transition: stroke-dasharray 0.7s linear 0s;
}

.progress-text {
	width: 100%;
	position: absolute;
	top: 60px;
	text-align: center;
	font-size: 2em;
}
.largelabel {
      display: inline-block;
      font: bold 1.05rem sans-serif;
      margin-bottom: 0.5rem;
  } 
    
  </style>