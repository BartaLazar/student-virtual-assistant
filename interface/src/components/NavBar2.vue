<template>
  <nav class="navbar navbar-expand-lg" id="nav">
      <div class="container-fluid" >
      <a href="#" class="navbar-brand">
      <!-- Logo Image -->
      <img src="../assets/logonom.png" width="50" alt="" class="d-inline-block align-middle mr-2"></a>
      <router-link to="/calendar" tag="button" ><button v-bind:class="{'white': !clicked, 'black': clicked}"
  v-on:click ="clicked = !clicked" class="btnicon1" @click="submit" id="btn"><font-awesome-icon class="calendericon2" icon="calendar-days" /></button></router-link>
      <router-link to="/liste" tag="button"><button v-bind:class="{'white': !clicked2, 'black': clicked2}"
  v-on:click ="clicked2 = !clicked2" class="btnicon2" @click="submit"><font-awesome-icon class="listicon2" icon="list-check" /></button></router-link>
      <button class="deconnexion"  @click="logout" type="submit">Deconnexion</button>
      </div>
  </nav>  
</template>

<script>
  import { BASE_PATH } from '@/common/common';
  import axios from 'axios';
  export default {
    name: 'NavBar2',
      data(){
          return{
              clicked: false,
              clicked2: false,
          }
      },
      methods: {
        logout(){
          const route = this.$router;
          const userId = localStorage.getItem("userId");
          axios.get(`${BASE_PATH}${userId}/disconnect/data`)
          .then((response) => {
                if(response.data["status_code"]== 200){
                    localStorage.clear();
                    alert("You are logged out");
                    route.push({ name:'home'});
                }
            })
     }
  },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body{
      background-color:white; 
      width:100%;
  }
  .navbar{
    background-color:#d80669;
    position:relative;
    width:100%;
    max-height: 100px;
  }
  nav{
    position: relative;
    top: 0;
    margin:auto;
  }
  img{
    width:120px;
    margin-left:0px;
  }
  .calendericon2{
    color:white;

  }
  .listicon2{
    color:white;
  }
  .deconnexion{
      background-color:black;
      width:10%;
      font-size:100%;
      height:35px;
      border:none;
      border-radius: 5px;
      color:white;
  }
  .deconnexion:hover{
    background-color:#b90b5c;;
  }
  
  .btnicon1{
      background-color:black;
      text-align: center;
      align-items:center;
      width:50%;
      max-height: 40px;
      border:none;
      font-size:27px;
      margin-right:70px;
  }
  .btnicon2{
     background-color:black;
      text-align: center;
      align-items:center;
      width:50%;
      max-height: 40px;
      border:none;
      font-size:27px;
      margin-right:70px;
  }
  .white{
      background-color:#d80669;
      color:white;
      
      
  }
  .black{
      background-color:#d80669;
      color:black;
  }

</style>