var count=0;

function increasevalue(id){
    console.log(id)
    count=document.getElementById(id).value;
    console.log(count)
    count++;
    document.getElementById(id).value=count;
};

function decreasevalue(id){
    count=document.getElementById(id).value;
    if(count==0){
        count=0;
    }
    else{
        count--;
    }
    document.getElementById(id).value=count;
};