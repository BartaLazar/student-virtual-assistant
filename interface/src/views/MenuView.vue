<template>
  <div class="menu">
    <NavBar/>
    <div class="buttonsmenu">
      <router-link to="/calendar" tag="button" ><div class="leftbutton"><button @click="submit"><font-awesome-icon class="calendericon" icon="calendar-days" /></button></div></router-link>
      <router-link to="/liste" tag="button"><div class="rightbutton" ><button @click="submit"><font-awesome-icon class="listicon" icon="list-check" /></button></div></router-link>
    </div>
  </div>
</template>


<script>
import NavBar from '@/components/NavBar.vue'
import Calendar from '@/components/Calendar.vue'
  export default {
    name: 'MenuView',
    components: {
      NavBar, 
    },
    created() {
    document.body.style.backgroundColor = "#FFFFFF";
  },
  }
</script>


<style>
body, html {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
}
button{
  border: none;
  padding: 5px;
  display: inline-block;
  font-size: 100px;
  height:300px;
  width:300px;
  cursor:pointer;
  margin: 4px 2px;
  border-radius:50%;
  transition:all 0.2s ease;
  border:none;
  background-color:#d80669;
}
.calendericon{
  font-size:80px;
  color:white;
}
.listicon{
  font-size:80px;
  color:white;
}
.leftbutton{
  /*text-align:left;*/
  display:inline-block;
  align-item:center;
  float:left;
  width:50%;
}
.rightbutton{
  /*text-align:right;*/
  display:inline-block;
  float:right;
  width:50%;


}
.buttonsmenu{
  text-align:center;
  margin-top:300px;
  
}

</style>