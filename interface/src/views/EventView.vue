<template>
    <div class="eventpage">
        <ListeComp/>
        <main>
            <h1 style="color:black;font-size: 30px;align-items: center;">Ajout d'événement/cours</h1>
            <form @submit.prevent="submitForm" v-if="!formSubmitted">
                <div >
                    <label class="largelabel">Nom</label>                        
                    <input 
                    v-model="course_name"
                    type="text"
                    placeholder="Nom du cours" 
                    />
                </div>
                <div >
                    <label class="largelabel">Code</label>
                    <!-- <input type="text" v-model="entry.content"> -->
                    <input 
                    v-model="course_id"
                    type="text"
                    placeholder="Code du cours" 
                    />
                </div>
                <div class="full-width">
                    <button class="btn3" @click="search" type="submit">Chercher dans PGC</button>
                </div>
                <div>
                    <label class="largelabel">Cours</label>
                    <select 
                    id="coursSelect"
                    v-model="courseSelected">
                        <option 
                        v-for="cours in cours" :value="cours.id_course"
                            >
                        {{ cours.course_name }}
                    </option>
                    </select>     
                </div>
                <div>
                    <label class="largelabel">Type</label>
                    <select 
                    id="typeSelect"
                    v-model="typeSelected">
                        <option 
                        v-for="cours in cours" :value="cours.id_course"
                            >
                        {{ cours.type }}
                        </option>
                    </select> 
                </div>
                <div>
                    <label class="largelabel">Jour</label>
                    <select 
                    id="jourSelect"
                    v-model="jourSelected">
                        <option 
                        v-for="cours in cours" :value="cours.id_course"
                            >
                        {{ cours.day }}
                        </option>
                    </select> 
                </div>
                <div>
                    <label class="largelabel">Début</label>
                    <input 
                        v-model="deb"
                        type="text"
                        placeholder="JJ/MM/AAAA" 
                    />
                </div>
                <div>
                    <label class="largelabel">Fin</label>
                    <input 
                        v-model="fin"
                        type="text"
                        placeholder="JJ/MM/AAAA" 
                    />
                </div>
                <div>
                    <label class="largelabel">De</label>
                    <input 
                        v-model="de"
                        type="text"
                        placeholder="HH/MM" 
                    />
                </div>
                <div>
                    <label class="largelabel">A</label>
                    <input 
                        v-model="a"
                        type="text"
                        placeholder="HH/MM" 
                    />
                </div>         
                <div>
                    <label class="largelabel">Régularité</label>
                    <input  
                        v-model="reg"
                        type="number"
                        placeholder="" 
                    />
                </div>
                <div>
              
                    <input 
                    type="checkbox"
                    id="choice"
                    v-model="toggle"
                    true-value="yes"
                    false-value="no"  />
                    <label for="choice" class="largelabel">Occurence unique</label> 
                </div>
                <div> 
                    <label class="largelabel">Salle</label>
                    <input 
                        v-model="salle"
                        type="text"
                        placeholder="Salle" 
                    />
                </div>
                <div>
                    <label class="largelabel">Batiment</label>
                    <input 
                        v-model="bat"
                        type="text"
                        placeholder="" 
                    />
                </div>
                <div>
                    <label class="largelabel">Professeur</label>
                    <input 
                        v-model="prof"
                        type="text"
                        placeholder="" 
                    />
                </div>
                <div>
                    <button class="btn4">Annuler</button>
                    <button @click="addevent()" class="submit" type="submit" value="Submit" >Ajouter</button>
                </div>
            </form>
        </main>
    </div>   
</template>



<script>
    import dropdown from 'vue-dropdowns';
    import ListeComp from '@/components/ListeComp.vue';
    import Select2 from 'vue3-select2-component';
    import {BASE_PATH} from '@/common/common.js';
    import axios from 'axios';
    export default {
        name: 'EventView',
        components: {
            ListeComp,
            'dropdown': dropdown,
            Select2,
  
        },
        created() {
            document.body.style.backgroundColor = "#FFFFFF";
        },
        methods:{
            myChangeEvent(val){
                console.log(val);
            },
            mySelectEvent({id, text}){
                console.log({id, text})
            },
            /*submitForm: function () {
                this.formSubmitted = true
            },*/
            search(){
                const userId = localStorage.getItem("userId");
                axios.get(`${BASE_PATH}${userId}/schedule/data/pgc?course_id=${this.course_id}&course_name=${this.course_name}`)
                .then((response) => {
                if(response.data["status_code"] == 200 || response.data["status_code"] == 201){
                    this.cours = response.data.events;
                    console.log("testtt", this.cours)
                }})
            },
            addevent(){
                const userId = localStorage.getItem("userId");
                axios.post(`${BASE_PATH}${userId}/course/data`,{
                    name: this.course_name,
                    course_code: this.course_id,
                    type : this.typeSelected,
                    day : this.jourSelected,
                    beginning_date : this.deb,
                    end_date : this.fin,
                    beginning_time : this.de,
                    end_time : this.a,
                    regularity : this.reg,
                    unique_occurrence : this.toggle,
                    room : this.salle,
                    building : this.bat,
                    teachers_full_name :this.prof,
                })
                .then((response)=>{
                    if(response.data["status_code"]== 200 || response.data["status_code"]== 201){
                        alert(response.data["instanciate tasks"]["message"]);
                        console.log("Sucess", response);
                        route.push({ name: 'calendar' })
                        
                    }
                    else{
                        alert("incorrect");
                        this.course_name="";
                        this.course_id="";
                        this.typeSelected="";
                        this.jourSelected="";
                        this.deb="";
                        this.fin="";
                        this.de="";
                        this.a="";
                        this.reg="";
                        this.toggle="";
                        this.salle="";
                        this.bat="";
                        this.prof="";
                    }
                })
        },
        methodToRunOnSelect(payload) {
            this.object = payload;
          },
          handleWeekendsToggle() {
            this.calendarOptions.weekends = !this.calendarOptions.weekends // update a property
        },
    },
    data() {
            return {
                deb: "",
                fin: "",
                de: "",
                a: "",
                reg: "",
                salle: "",
                bat: "",
                prof: "",
                myValue: '',
                courseSelected:'',
                cours:[],
                typeSelected:'',
                jourSelected:'',
                myOptions:['op1', 'op2', 'op3'],
                myOptions2:['op12', 'op22', 'op32'],
                arrayOfObjects: ['laila', 'lilo'],
                object: {
                name: 'Object Name',
                },
                toggle: [],
                status: 'not_accepted',
                calendarOptions: {
                weekends: true,
                
                /* you can update a remote database when these fire:
                eventAdd:
                eventChange:
                eventRemove:
                */
            },
                //formSubmitted: false
            };
        },
    }

</script>

<style>
    body {
        margin: 0;
        background-color: hsl(0, 0%, 98%);
        color: #333;
        font: 100% / normal sans-serif;
    }

    main {
        margin: 0 auto;
        padding: 4rem 0;
        width: 90%;
        text-align: center;
    
    }

    .full-width {
        grid-column: span 2;
    }
    span,
    input{
        font-size: 1.5rem;
        line-height: 0.8;
    }
    .my-dropdown-toggle{
        padding: 4px 8px;
        margin: 2px;
        background-color:white;
        border-radius: 3px;
        border:none;
        width:160px;
    }

    input
    {
        padding: 0.4rem;
        width: 100%;
        border:none;
        border-radius: 3px;
        border:0.5px solid grey;
    }
    .btn3{
        font-size: 1.2rem;
        line-height: 1;
        background: #a3a3ab;
        color: #fff;
        border: none;
        width:100%;
        border-radius:3px;
        padding: 0.6rem;
    }

    .btn4{
        font-size: 1.2rem;
        line-height: 1;
        margin-right:1rem;
        margin-top: 0rem;
        background: #a3a3ab;
        color: #fff;
        border: none;
        width:30%;
        border-radius:3px;
        padding: 0.6rem;
        float:left;
    }
    .submit{
        font-size: 1.2rem;
        line-height: 1;
        margin-top: 0rem;
        background: #d80669;
        color: #fff;
        border: none;
        width:52%;
        border-radius:3px;
        padding: 0.6rem;
        float:right;
    }

    button:hover,
    button:focus {
    background: #5a5b6e
    }
    form{
        background-color: pink;
        width: 50em;
        margin: 0 auto;
        
        box-sizing: border-box;
        padding: 2rem;
        border-radius: 1rem;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;

        
    }
    .full-width {
    grid-column: span 2;
    }
  button,
  input,
  textarea {
      -webkit-appearance: none;
      -moz-appearance: none;
      appearance: none;
      background-color: transparent;
      border: none;
      padding: 0;
      margin: 0;
      box-sizing: border-box;
  }
  input,
  select,
  button{
    border-radius: 3px ;
    border:solid rgb(150, 149, 149);
    background-color: rgb(255, 255, 255);
    border-radius: 0.25rem;
  
  }
  input[type="text"],
  select,
  textarea,
  button {
  font: 1rem / 1.5 sans-serif;
  display: block;
  box-sizing: border-box;
  width: 100%;
  padding: 0.5rem 0.75rem;
  }
  input:focus,
  select:focus{
      outline: none;
      box-shadow: 0 0 0 4px #d80669;
  }
  
  .largelabel {
      display: inline-block;
      font: bold 1.05rem sans-serif;
      margin-bottom: 0.5rem;
  } 
 
    input[type="checkbox"] {
        height: 1.5em;
        width: 1.5em;
        vertical-align: middle;   
    }
    input[type="radio"]:checked {
        background-image: radial-gradient(
            hsl(213, 73%, 50%) 40%,
            transparent calc(40% + 1px)
        );
    }
    

  


</style>
