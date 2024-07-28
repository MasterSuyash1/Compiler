<template>
    <h1 class="mainhead">TecUP Compiler</h1>
    <div @keydown="this.useTab" class="main">
        <div class="program">
            <div class="destop_top_bar">
               <div class="code">CODE</div>
               <div class="just">
                    <div class="run"> <input type="submit" @click="this.run" :value="this.state" :disabled="this.running" id="RUN"></div>
                    <select v-model="this.lang" name = "lang" id="lang" required>
                      <option disabled value="" >--Select--</option>
                      <option value="c" >C</option>
                      <option value="cpp" >C++</option>
                      <option value="py">Python 3.8</option>
                      <option value="java" >Java</option>
                      <option value="r" >R</option>
                      <option value="js" >JavaScript</option>
                    </select>
                </div>
            </div>
            <div>
            <textarea spellcheck="false" name="code" id="code" cols="100" rows="150" placeholder="Write your code here..." v-model="code"></textarea>
            </div>
        </div>
        <div class="output">
            <div class="terminal_top_bar">
                <div class="console" >CONSOLE</div>
                <div class="clear" @click="this.out=''"><input type="submit" value="CLEAR" id="CLEAR"> </div>
            </div>
            <div>
            <textarea spellcheck="false" name="out" :class="{error_red : err}" id="out" cols="120" rows="50" v-model="out" readonly></textarea>
            </div>
        </div>
    </div>
</template>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Inconsolata&family=Roboto+Slab&display=swap');
  .error_red{
    color : #cf6679 !important;
  }
  *{
    box-sizing: border-box;
    transition: 0.4s ease-in;
}

body{
  background: #c31432;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #240b36, #c31432);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #240b36, #c31432); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */



    font-family: Verdana, Geneva, Tahoma, sans-serif;
    margin: 10px 0px 0px 0px;
    font-size: 17px;
    padding: 8px;
    /* background-color:#000000; */
    color : white;
    width: 100%;
}
.mainhead {
    display: flexbox;
    font-family: 'Roboto Slab', serif;
    text-align: center;
    font-weight: lighter;
}
.main{
    width: 100%;
    display: flex;
    padding: 0px 0px 0px 10px;
    gap:10px;
}


.program{
    display: flex;
    overflow: visible;
    margin: 2px 2px 0px 0px;
    display: inline-block;
    padding: 5px 20px 15px 20px;
    border-top: 1px solid rgba(211, 211, 211, 0.377);
    border-right: 2px solid rgba(211, 211, 211, 0.377);
    border-left: 1px solid rgba(211, 211, 211, 0.377);
    border-bottom: 1px solid rgba(211, 211, 211, 0.377);
    width: 50%;
}
.destop_top_bar{
    display: flex;
    padding: 0px 0px 12px 0px;
    border-bottom: 1px solid rgba(211, 211, 211, 0.377);
    width: 100%;
    height: 1.2cm;
    
}
.just{
    display: flex;
    justify-content:space-between;
    width: 100%;
    padding: 0px 2px 0px 2px;
}
.code{
    display: inline-block;
    text-align: center;
    width: 1in;
    margin-right:5px;
    border-right: 1px solid black;
    padding: 2.3%;
}

.run{
    margin-left: 0px 5px 5px 5px 5px;
    display: inline-block;
    text-align: center;
    width:1in;
    
}
input[type="submit"]{
    background-color: #4daea1;
    
    padding: 6px 15px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    width: auto;
}
input[type="submit"]:hover{
    background-color: #08462b;
}


.output{
    display: flex;
    overflow: visible;
    margin: 2px 2px 0px -4px;
    display: inline-block;
    padding: 5px 20px 15px 20px;
    border-top: 1px solid rgba(211, 211, 211, 0.377);
    border-right: 1px solid rgba(211, 211, 211, 0.377);
    border-left: 2px solid rgba(211, 211, 211, 0.377);
    border-bottom: 1px solid rgba(211, 211, 211, 0.377);
    
}



.terminal_top_bar{
    width: fit-content;
}
    .terminal_top_bar{
        display: flex;
        padding: 0px 5px 5px 5px;
        border-bottom: 1px solid black;
        width: 100%;
        height: 1.2cm;
        
    }
    .console{
        display: inline-block;
        align-items: center;
        text-align: center;
        width: 1.2in;
        margin-right:0px 5px 5px 5px;
        border-right: 1px solid black;
        padding: 2.5% 2.5% 2.5% 0%;
    }
    
    .clear{
        display: inline-block;
        margin-left: 5px;
        display: inline-block;
        text-align: center;
        width:1in;
        
    }
    input[type="submit"]{
        background-color: #6728b4;
        color: white;
        font-weight: 700;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        width: auto;
        transition: 0.4s;
    }
    input[type="submit"]:hover{
        background-color: #3b0e74;
    
        
    }
  textarea{
    width: 100%;
    height: 50%;
    padding: 10px;
  }

  #out{
    background-color: black;
    font-weight: 700;
    color:white
  }
  
  .output, .program{
    padding-top: 10px;  
    border-radius: 8px;
    background-color: #121212;
}


.code, .console {
  border-color: rgba(211, 211, 211, 0.377);
}

.output, .program{
  border: none;
}

.program:focus, .output:focus{
  border: none;
}

#code{
  font-family: 'Inconsolata', monospace;
  background-color: #121212;
  border: none;
  color: rgb(255, 255, 255);
}

#lang{
  background-color: #00000000;
  color: white;
  border: 1px solid rgba(211, 211, 211, 0.377);
}
option{
  background-color: #121212;
}


</style>

<script>
  export default{
    name:"App",
    data(){
      return{
        code:"",
        running : false,
        out:"",
        err:false,
        night : false,
        lang: localStorage.getItem("lang") ?  this.lang=localStorage.getItem("lang") : "",
        BACKEND : "http://127.0.0.1:5000/" ,
        boiler : {
          'py' : '',
          'js' : '',
          'r' : '',
          'java': `class main{
    public static void main(String[] args) {

        // Your code here 

    }
}`,
          'cpp' : `#include <iostream>
using namespace std;

int main(){

    // Your code here

    return 0;
}`,
          'c' : `#include <stdio.h>

int main(){
    // Your code here 

    return 0;
}`
        }
      }
    },
    methods:{
      run : function(){
        if (!this.lang ){
          alert("Please select a language !!")
          return
        }
        else if(!this.code){
          alert("Empty input !!")
          return
        }
        this.out=""
        this.running=true;
        fetch(this.BACKEND, {
            method : 'post',
            body : JSON.stringify({
                code : this.code,
                lang : this.lang
            })
        })
        .then(res => res.json())
        .then(data => {
            if(data.output.err){
              console.log("hi")
              this.err=true;
              this.out=data.output.msg
            }
            else{
              this.out=data.output;
              this.err=false;
            }  
            this.running=false;
        })
      },
      useTab : function(e){
        if (e.key == 'Tab') {
          e.preventDefault();
          var start = e.target.selectionStart;
          var end = e.target.selectionEnd;
      
          // set textarea value to: text before caret + tab + text after caret
          e.target.value = e.target.value.substring(0, start) +
            "\t" + e.target.value.substring(end);
      
          // put caret at right position again
          e.target.selectionStart =
            e.target.selectionEnd = start + 1;
        }
      }
    },
    computed: {
      state : function(){
        if (this.running){
          return "Running.."
        }
        else{
          return "RUN"
        }
      }
    },
    watch:{
    lang : function(n){
      this.code=this.boiler[n];
      localStorage.setItem("lang",n)
    }
  }
}
  
</script>