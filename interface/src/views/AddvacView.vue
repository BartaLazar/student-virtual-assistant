<template>
    <div class="addvacpage">
        <ListeComp/>
        <main>
        <h1 style="color:black;font-size: 30px;align-items: center;">Ajout de vacances</h1>
            <form @submit.prevent="submitForm" v-if="!formSubmitted">
               
                <div>
                    <label class="largelabel">Nom</label>
                    <input v-model="nom"
                        type="text"
                        placeholder="HH/MM" />
                </div>
                <div>
                    <label class="largelabel">De</label>
                    <input 
                        v-model="de"
                        type="text"
                        placeholder="HH/MM"/>
                </div>
                <div>
                    <label class="largelabel">A</label>
                    <input 
                        v-model="a"
                        type="text"
                        placeholder="HH/MM"/>
                </div>  
                <div class="full-width">
                    <button class="btn4">Annuler</button>
                    <button @click="addholiday()" class="submit" type="submit" value="Submit" >Ajouter</button>
                </div>
            </form>
        </main>
    </div>   
</template>



<script>
    import ListeComp from '@/components/ListeComp.vue';
    import {BASE_PATH} from '@/common/common.js';
    import axios from 'axios';
    export default {
        name: 'AddvacView',
        components: {
            ListeComp,
  
        },
        created() {
            document.body.style.backgroundColor = "#FFFFFF";
        },
        methods: {
            addholiday(){
                this.formSubmitted = true;
                const route = this.$router;
                const userId = localStorage.getItem("userId");
                axios.post(`${BASE_PATH}${userId}/events/holiday/data`,{
                    start_date : this.de,
                    end_date : this.a
                })
                .then((response)=>{
                if(response.data["status_code"]== 200 || response.data["status_code"]== 201){
                    alert(response.data["message"]);
                    console.log("Sucess", response);
                    route.push({ name: 'calendar' })      
                }
                else{
                    this.de="";
                    this.a="";
                }
            })
            },
            submitForm: function () {
                this.formSubmitted = true
            },
            methodToRunOnSelect(payload) {
                this.object = payload;
            }
        },
        data() {
        return {
            nom: "",
            de: "",
            a: "",
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