<template>
    <div class="taskpage">
        <ListeComp/>
        <main>
        <h1 style="color:black;font-size: 30px;align-items: center;">Ajout de tâche</h1>
        <form @submit.prevent="submitForm" v-if="!formSubmitted">
                <div class="full-width">
                    <label  class="largelabel">Description</label>
                    <textarea v-model="description"  id="description"></textarea>
                </div>
                <div>
                    <label class="largelabel">Type</label>
                    <select v-model="typetaskSelected" style="width:100%;align-items: center;">
                        <option v-for="option in tasktypes" :value="option.type">
                            {{ option.type }}
                        </option>
                    </select>
                    <!-- <select 
                    id="typeSelect"
                    v-model="typetaskSelected">
                        <option 
                        v-for="task in tasktypes" :value="tasktypes.type"
                            >
                        {{ task.type }}
                        </option>
                    </select>  -->
                </div>
                <div >
                        <label class="largelabel">Délai</label>                        
                        <input 
                        v-model="delaitask"
                        type="text"
                        placeholder="JJ/MM/AAAA"
                    />
                    </div>
                    <div>
                        <button class="btn4">Annuler</button>    
                        <router-link to="/modif" tag="button">
                            <button @click="addtask()" class="submit" type="submit" value="Submit" >Ajouter</button>
                        </router-link>
                    </div>
        </form>
    </main>
    </div>   
</template>

<script>
    import Select2 from 'vue3-select2-component';
    import ListeComp from '@/components/ListeComp.vue';
    import {BASE_PATH} from '@/common/common.js';
    import axios from 'axios';
    export default {
        name: 'TaskView',
        components: {
            ListeComp,
            Select2
  
        },
        created(){
            document.body.style.backgroundColor = "#FFFFFF";
            const userId = localStorage.getItem("userId");
            axios.get(`${BASE_PATH}${userId}/tasks/types/data`)
            .then((response) => {
            if(response.data["status_code"] == 200 || response.data["status_code"] == 201){
                this.tasktypes = response.data.data
                console.log("testtypes",this.tasktypes)
            }})
            
                // const userId = localStorage.getItem("userId");
                // axios.get(`${BASE_PATH}${userId}/tasks/types/data`)
                // .then((response) => {
                //     if(response.data["status_code"] == 200 || response.data["status_code"] == 201){
                //         this.tasktypes = response.data.data;
                //         console.log("test tasktypes", this.tasktypes)
                //     }})
            
        },
        
        // methods: {
        // submitForm: function () {
        //     this.formSubmitted = true
        // },
        // methodToRunOnSelect(payload) {
        //     this.object = payload;
        //   }
        // },
        // data(){
        // return{
        //     myValue: '',
        //     type:['type1', 'type2', 'type3'],
        // }
        // },
        methods:{
            addtask(){
                const userId = localStorage.getItem("userId");
                axios.post(`${BASE_PATH}${userId}/course/tasks/data`,{
                    type : this.typetaskSelected,
                    description : this.description,
                    due_date : this.delaitask
                })
                .then((response)=>{
                if(response.data["status_code"]== 200 || response.data["status_code"]== 201){
                    alert(response.data["description"]);
                    console.log("Sucess", response);
                    route.push({ name: 'calendar' })
                      
                }
                else{
                    
                    this.typetaskSelected ="";
                    this.description ="";
                    this.delaitask ="";
                }
            })
            },
            myChangeEvent(val){
                console.log(val);
            },
            mySelectEvent({id, text}){
                console.log({id, text})
            }
        },
        data() {
        return {
            description:"",
            del: "",
            tasktypes:[],
            arrayOfObjects: ['laila', 'lilo'],
            object: {
              name: 'Object Name',
            },
            typetaskSelected: '',
            formSubmitted: false
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
    
    .my-dropdown-toggle{
        padding: 4px 8px;
        margin: 2px;
        background-color:white;
        border-radius: 3px;
        border:none;
        width:160px;
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
        min-height: 40vh;
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
  button,
  textarea{
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
  textarea {
    min-height: 7rem;
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

  


</style>
