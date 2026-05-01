<template>
    <div class="login">
      <NavBar/>
      <form @submit.prevent="submitForm" v-if="!formSubmitted">
                <div class="content">
                    <h1 style="color:black;font-size: 30px;text-align: center;">Se connecter</h1>
                    <div><span>Email</span>
                    <input 
                        v-model="email"
                        type="text"
                        placeholder="Votre nom" 
                    /></div>
                    
                    <div><span>Mot de passe</span>
                    <input 
                        v-model="mdp"
                        type="password"
                        placeholder="votre mot de passe" 
                    /></div>
                            <button class="submit" type="button" value="Submit" @click="submitForm" >Confirmer</button>        
                </div>
            </form>
    </div>
    
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import {BASE_PATH} from '@/common/common.js';
import axios from 'axios';
export default {
  name: 'LoginView',
  components: {
    NavBar
  },
  created() {
        document.body.style.backgroundColor = "white";
    },
  data(){
        return {
            email: "",
            mdp: "",
            formSubmitted: false
        };
        },
    methods: {
        submitForm: function () {
            //this.formSubmitted = true;
            const route = this.$router;//put it outside everytime 
            //console.log("router", this.$router)
            axios.post(`${BASE_PATH}connect/data`, {
                email: this.email,
                password: this.mdp
            })

            .then((response) => {
                if(response.data["status_code"]== 200 || response.data["status_code"]== 201){
                    localStorage.setItem("userId",response.data.user_id);
                    alert("Vous êtes bien connecté");
                    console.log("Sucess", response);
                    route.push({ name: 'menu' })
                      
                }
                else{
                    alert("incorrect");
                    this.email = "";
                    this.mdp = "";
                }
                
            })
            .catch((error) => {
                console.log("Fail", error);
            });
            },
            methodToRunOnSelect(payload) {
                this.object = payload;
            }
        },
}
</script>
<style scoped>
html,body {
        padding: 0;
        margin: 0;
        width: 100%;
        min-height: 100vh;
        font-family: system-ui, sans-serif;
    }
    span,
    input{
        font-size: 1.5rem;
        line-height: 0.8;
    }
    .content{
        padding:10px;
    }
    form {   
        width: 30em;
        max-width: 90%;
        text-align:left;
        max-width: 90%;
        margin: 0 auto;
        align-items: center;
        min-height: 100vh;
        /* nice thing of auto margin if display:flex; it center both horizontal and vertical :) */
            }
    .signup{
        width: 100%;
    }

    form div {
        margin-top: 3rem;
    }

    span {
        margin-bottom: 0.4rem;
        display: block;
        color:black;
    }
    
    input
    {
        padding: 0.4rem;
        width: 100%;
        border:none;
        border-radius: 3px;
        border:0.5px solid grey;
    }
    
    .submit{
        font-size: 1.2rem;
        max-height: 50px;
        margin-top: 0rem;
        background: #d80669;
        color: #fff;
        border: none;
        width:52%;
        border-radius:3px;
        padding: 0.6rem;
        margin-top:2rem;;
        float:right;
    }
</style>
