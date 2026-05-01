<template>
    <div class="signup">
        <NavBar/>
        <form @submit.prevent="submitForm" v-if="!formSubmitted" >
                <div class="content">
                    <h1 style="color:black;font-size: 30px;align-items: center;">Créer un compte </h1>
                    <div><span>Nom</span>
                    <input 
                        v-model="name"
                        type="text"
                        placeholder="Votre nom" 
                    /></div>
                    <div><span>Prenom</span>
                    <input 
                        v-model="firstname"
                        type="text"
                        placeholder="Votre nom" 
                    /></div>
                    <div><span>Mot de passe</span>
                    <input 
                        v-model="mdp"
                        type="password"
                        placeholder="votre mot de passe" 
                    /></div>
                    <div><span>Email</span>
                    <input 
                        v-model="email"
                        type="text"
                        placeholder="Votre email" 
                    /></div>
                    <div><span>Cursus</span>
                    <input 
                        v-model="cursus"
                        type="text"
                        placeholder="degree/year/program" 
                    /></div>
                        <button class="submit" type="submit" value="Submit" >Confirmer</button>
                </div>
            </form>
    </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue'
import axios from "axios"
import { BASE_PATH } from '@/common/common';
export default {
    name: 'SignupView',
    components: {
        NavBar
    },
    created() {
        document.body.style.backgroundColor = "white";
    },
    data(){
        return {
            name: "",
            firstname: "",
            mdp: "",
            email: "",
            cursus:"",
            formSubmitted: false
        };
        },
    methods: {
        
        /*async submitForm() {
            this.formSubmitted = true;
            let result = axios.post("http://127.0.0.1:5000/signup/data",{
                email: this.email, 
                password: this.mdp,
                family_name:this.name,
                first_name: this.firstname,
                cursus: this.cursus
            });

            console.warn(result);
            if(status_code ==201){
                alert("sign-up done");
                localStorage.setItem("user-info", JSON.stringify(result.data));
                this.$router.push({name:menu})

            }
            
        },*/
        submitForm: function () {
            this.formSubmitted = true;
            const route = this.$router;
            //const path = 'http://127.0.0.1:5000/signup/data'
            axios.post(`${BASE_PATH}signup/data`, {
                email: this.email, 
                password: this.mdp,
                family_name:this.name,
                first_name: this.firstname,
                cursus: this.cursus,
            })
            .then(response=>{
                if(response.data["status_code"]== 201){
                    console.log("Sucess");
                    alert("compte est bien crée");
                    route.push({name:'menu'})
                }
            })
            }
            // status code 200 et 201 succes, verifier le status code apres chaque requette 
            },
            methodToRunOnSelect(payload) {
                this.object = payload;
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
        line-height: 1;
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
