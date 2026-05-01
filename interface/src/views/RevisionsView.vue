<template>
    <ListeComp/>
    <br>
    <div class="buttonsadd">
        <router-link to="/task" tag="button"><button class="addtask" @click="submit">Ajouter une séance de révision</button></router-link>
    </div>
    <br>
    <hr>
    <br>
    <div class="box">
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
    </div>
    
    <main>
     <form>
      
        <div
      v-for="(entry, index) in list"
      :key="index"
    >
    <input 
            type="checkbox"
            id="choice"
            v-model="toggle"
            true-value="yes"
            false-value="no"  />
        <label class="largelabel">{{entry.column_name}}</label>
        <br>
        <br>
        <br>
        <!-- <input type="text" v-model="entry.content"> -->
        <!-- <input type="text" v-model="entry.content">  -->
      
    </div>
    <!-- clicking on this button the user will give up the changes that he made and he will be directed to the page that contains the table -->
    
  </form>   
    </main>
  </template>
  
  <script>
  import { ref } from 'vue'
  import ListeComp from '@/components/ListeComp.vue';
  import axios from "axios"
  import { BASE_PATH } from '@/common/common';
  import { ElementTypes } from '@vue/compiler-core';
  export default {
    name: 'Revisions',
    components:{
        ListeComp
    },
    setup(){
        const completedRevs = ref(0);
        const totalRevs = ref(10);
        const startColor = ref('#d80669');
        const stopColor	= ref('#d80669');
        const innerStrokeColor = ref("#e08bb3")
        return {
            completedRevs,
            totalRevs,
            startColor,
            stopColor,
            innerStrokeColor
            }
    },
    
    created(){  
    //   const lineId = localStorage.getItem("selectedLineid");
    //   const refId = localStorage.getItem("refId");
    //   const sessionKey = localStorage.getItem("sessionKey");
      
      ///{session_key}/referentials/{ref_id}/data?line={line_id}
    //   axios.get(`${BASE_PATH}${sessionKey}/referentials/${refId}/data?line_id=${lineId}`)
    //   .then(response=>{
    //     if(response.data["status_code"]== 200){
    //       console.log("this is lineid",lineId);
    //       console.log("Sucess2",response.data.data);
    //       const elements = response.data.data;
    //       console.log("elements",elements);
    //       const clonnedList = [];
    //       for ( let i=0; i<elements.length; i++){
    //         console.log("item", elements[i])
    //         clonnedList.push(elements[i])
    //       //  list.assign(elements[i])
    //       //  console.log("list", list)
    //       }
    //       this.list = clonnedList;
    //     }
    //     else{
    //       alert(response.data["message"])
    //       this.$router.push({name: "rechercheref"})
    //     }
        
    //     // console.log(list);
    //     //{"data" : [{"column_name" : String,"content" : String},...]}
    //   })
    },
    methods:{
    //   saveChanges(){
    //     console.log("List from submit", this.list)
    //     const refId = localStorage.getItem("refId");
    //     const route = this.$router;
    //     const lineId = localStorage.getItem("selectedLineid");
    //     const updatedData = this.list.map(row => ({...row, line_id: lineId}));
    //     const sessionKey = localStorage.getItem("sessionKey");
    //     axios.put(`${BASE_PATH}${sessionKey}/referentials/${refId}/data`,{
    //       data: updatedData,
    //       //this.column_name = ;
    //       //content : this.inputDetails[entry.column_name];
    //     })
    //     .then(response=>{
    //       if(response.data["status_code"] == 200 || response.data["status_code"] == 201){
    //         alert("Les changements sont enregistrés");
    //         console.log("Response", response);
    //         route.push({ name:'rechercheref'});
    //       }
    //       else{
    //         alert(response.data["message"])
    //       }
          
  
    //     })
    //   }
    },
    data(){
        return {
          //list,
          list: [],
          list: [
            {
            "column_name": "séance1", "content": "value"},
            {
            "column_name": "séance2",
            "content": "id"},
            {
            "column_name": "séance3",
            "content": "idee"},
            {
            "column_name": "séance4",
            "content": "idrr"},
            ],
            inputDetails: {},
            toggle: [],
        }
    },
  }
  </script>
  <style scoped>
  
  main {
    margin: 0 auto;
    padding: 4rem 0;
    width: 90%;
    max-width: 60rem;
    }
  
  form{
    box-sizing: border-box;
    padding: 2rem;
    border-radius: 1rem;

    grid-template-columns: 1fr 1fr;
   
    align-items:center;
  }
    .full-width {
        grid-column: span 2;
    }
    .midwidth{
        grid-column: span 1;
        margin-top:10px;
    }
  
    button,
    input,
    select,
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
    hr{
      width:70%;
      align-items: center;
      margin:auto;
    }
    
    .addtask{
        background-color:#d80669;
        border-radius: 3px;
        border:0.5px solid ;
        height: 50px;
        width:330px;
        color:white;
    }
    .buttonsadd{
      float:right;
      margin-right:100px;
    }
    .box{
      display: flex;
      align-content:center;
      justify-content: center;
      border-radius: 4px;
      margin:auto;
      width:80%;
      float: left;
     
    }
    input,
    select{
    border-radius: 3px ;
    border:solid rgb(150, 149, 149);
    background-color: white;
    border-radius: 0.25rem;
    
    }
    input[type="text"],
    select,
    textarea {
    font: 1.25rem / 1.5 sans-serif;
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
    button{
        font: 1.25rem sans-serif;
        border-radius: 3px ;
        border:solid rgb(104, 102, 102);
        cursor: pointer;
        padding: 0.75rem 1.25rem;
        width:48%;
        margin-left:8px;
        
    }
    .largelabel {
        display: inline-block;
        font: bold 1.2rem sans-serif;
        margin-bottom: 0.5rem;
    }
  
    button[type="submit"] {
        background-color:#d80669;
        color: white;
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