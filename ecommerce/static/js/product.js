var count=0;

function increasevalue(){
    count=document.getElementById('display').value;
    console.log(count)
    count++;
    document.getElementById('display').value=count;
};

function decreasevalue(){
    count=document.getElementById('display').value;
    if(count==0){
        count=0;
    }
    else{
        count--;
    }
    document.getElementById('display').value=count;
};