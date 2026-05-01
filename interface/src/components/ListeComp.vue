<template>
    <div class="listecomponent">
        <NavBar2/>
        <div class="uperdiv">
           <p class="cours">Cours</p> 
        </div>
        <div class="left_wrap">
            <select v-model="selected" style="width:100%;align-items: center;" @change="handleChange">
            <option v-for="option in options" :value="option.color">
                {{ option.course_name }}
            </option>
            </select>
            <!-- <div>Selected: {{ selected }}</div> -->
        </div>
    </div>
  
</template>
  
  <script>
  // @ is an alias to /src
  import NavBar2 from '@/components/NavBar2.vue'
  import {BASE_PATH} from '@/common/common.js';
  import axios from 'axios';
  import { ModelListSelect } from 'vue-search-select'
  export default {
    name: 'ListeComps',
    components: {
      NavBar2,
      ModelListSelect
    },
    created() {
        document.body.style.backgroundColor = "#FFFFFF";
        const userId = localStorage.getItem("userId");
            axios.get(`${BASE_PATH}${userId}/course/data`)
            .then((response) => {
              if(response.data["status_code"] == 200 || response.data["status_code"] == 201){
                this.options = response.data.data
                console.log("test created function",this.options)
                console.log(response.data.data.course_id)
                const elements = response.data.data
                const courses = [];
                for ( let i=0; i<elements.length; i++){
                console.log("item", elements[i])
                // courses.push(elements[i])
                // //  list.assign(elements[i])
                // console.log("list", this.courses)
                localStorage.setItem("courseId", elements[i].course_id);
                localStorage.setItem("coursecolor", elements[i].color);
                }
              }})
    },
    
    data(){
        return{
            myValue: '',
            coursofstudent:[],
            liste:[],
            selected: '',
            options: [],
            item:''
        }
    },
    methods:{
        // handleChange(e){
        //     const userId = localStorage.getItem("userId");
        //     axios.get(`${BASE_PATH}${userId}/course/data`)
        //     .then((response) => {
        //       if(response.data["status_code"] == 200 || response.data["status_code"] == 201){
        //         localStorage("courseId", response.data.data["course_id"])
        //       }})
        // },
        myChangeEvent(val){
            console.log(val);
        },
        mySelectEvent({id, text}){
            console.log({id, text});
        },
        handleChange(event){
            const route = this.$router;
        //     this.selected = event.target.options[event.target.options.selectedIndex].text
            route.push({ name: 'liste' })
        }
    } 
  }
  </script>
  <style>
    .left_wrap {
        min-height: 100vh;
        width:20%;
        background-color:#d80669;
        overflow:scroll;
        float: left;
       
    }
    input,
  select{
    border-radius: 3px ;
    border:solid rgb(150, 149, 149);
    background-color: rgb(255, 255, 255);
    border-radius: 0.25rem;
  
  }
  input[type="text"],
  select{
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
  
    body, html {
        padding: 0;
        margin: 0;
        width: 100%;
        min-height: 100vh;
    }
    .btn{
        background-color:#ac0f58;
        border:none;
        height:40px;
        width: 80%;

    }
    .btn:hover{
        background-color:#d80669;
    }
    .dropdown{
        margin:auto;
        margin-top:10px;
    }
    .uperdiv{
        height:35px ;
        width:100%;
        background-color:lightgray;
    }
    .cours{
        color:#d80669;
        font-size:25px;
        margin:auto;
       
    }

  </style>
  