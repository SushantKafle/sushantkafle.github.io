
var dynamicBackground = {
    
    number:25,
    
    X:[],
    Y:[],
    
    incX:[],
    incY:[],
    
    color:['#ef0fff','#0eff00','#aaffff','#e009ff','#aaff55'],
    
    init: function(){
        
        width=$(window).width();
        height=$(window).height();
        
        var canvas = document.getElementById('canvasSection');
        canvas.height = height;
        canvas.width = width;
        
        //$("#canvasSection").css('margin-top', -3*height);
        //$("#canvasSection").css('background', "#000");
        
        val = [-1,1];
        
        for(i=0;i<this.number;i++)
        {
            this.X[i] = Math.floor(Math.random()*width);
            this.Y[i] = Math.floor(Math.random()*height);
            
            
            this.incX[i] = val[Math.floor(Math.random()*2)];
            this.incY[i] = val[Math.floor(Math.random()*2)];
        }
    },
    
    draw: function(){
        //May be perlin noise implementation
        var canvas = document.getElementById('canvasSection');
        var context = canvas.getContext('2d');

        for(i=0;i<this.number;i++)
        {
            context.fillStyle=this.color[i%5];
            context.fillRect(this.X[i], this.Y[i],7,7);
        }
        
        

    },
    
    clear: function(){
        
        var canvas = document.getElementById('canvasSection');
        var context = canvas.getContext('2d');
        context.fillStyle = '#fff';
		context.fillRect(0,0,$("#canvasSection").width(),$("#canvasSection").height());
    },
    
    animate: function(){
        
        
        for(i=0;i<this.number;i++)
        {
            
            if(this.Y[i] > $(window).height() || this.Y[i] < 0)
            {
                this.incY[i] = this.incY[i] * -1;
            }
            
            if(this.X[i] > $(window).width() || this.X[i] < 0 )
            {
                this.incX[i] = this.incX[i] * -1;
            }
            
            
            this.X[i] += this.incX[i];
            this.Y[i] += this.incY[i];
        }
        
        this.clear();
        this.draw();
    },
    
    circle: function(x,y,radius){
        
    }
    
    
}