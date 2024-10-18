//In creating this game, I have used Youtube tutorials, Udemy, geeksforgeeks, w3schools, tutorialspoint, and other resources to help me understand the concepts of the game.
//I used AI as a precise search engine, and my VSCode is equipped with a debugging AI engine.
//This game is a take on the cult-favorite game Flappy Bird, with a twist by using my all-time favorite character, Pusheen the cat. (I still have a Pusheen plushie from I was 14 hehe).
//This game is a simple game where the player has to avoid the obstacles and collect the stars (which adds 5 extra points) to increase their score.
//The game is controlled by the spacebar key, which allows the player to jump over the obstacles.
//The game ends when the player hits the obstacles or goes out of bounds.
//The player can restart the game by pressing the Enter key.
//This game looks visually better when played as a half-screen than a full-screen.
//Extra: I have added a sound effect for when the player scores a point and when the player dies.
//Thank you for playing my game. I hope you enjoy it as much as I enjoyed making it.

let pusheen_speed = 3, gravity = 0.5;
let pusheen = document.querySelector('.pusheen');
let img = document.getElementById('pusheen-1');
let score_sound = new Audio('sounds effect/point.mp3');
let die_sound = new Audio('sounds effect/die.mp3');
let pusheen_attributes = pusheen.getBoundingClientRect();
let background = document.querySelector('.background').getBoundingClientRect();
let score_graphics = document.querySelector('.score_graphics');
let message = document.querySelector('.message');
let score_title = document.querySelector('.score_title');
let game_status = 'Start';
img.style.display = 'none';
message.classList.add('messageStyle');
document.addEventListener('keydown', (e) => {
    if(e.key == 'Enter' && game_status != 'Play'){
        document.querySelectorAll('.pipe_graphics, .star_graphics').forEach((e) => {
            e.remove();
        });
        img.style.display = 'block';
        pusheen.style.top = '40vh';
        game_status = 'Play';
        message.innerHTML = '';
        score_title.innerHTML = 'Score : ';
        score_graphics.innerHTML = '0';
        message.classList.remove('messageStyle');
        play();
    }
});
function play(){
    function move(){
        if(game_status != 'Play') return;
        let pipe_graphics = document.querySelectorAll('.pipe_graphics, .star_graphics');
        pipe_graphics.forEach((element) => {
            let graphics_attributes = element.getBoundingClientRect();
            pusheen_attributes = pusheen.getBoundingClientRect();
            if(graphics_attributes.right <= 0){
                element.remove();
            } else {
                if(pusheen_attributes.left < graphics_attributes.left + graphics_attributes.width && 
                   pusheen_attributes.left + pusheen_attributes.width > graphics_attributes.left && 
                   pusheen_attributes.top < graphics_attributes.top + graphics_attributes.height && 
                   pusheen_attributes.top + pusheen_attributes.height > graphics_attributes.top){
                    //If player hits the star, score increases by 5
                    if(element.classList.contains('star_graphics')){
                        score_graphics.innerHTML = +score_graphics.innerHTML + 5; 
                        element.remove(); 
                    } else {
                        game_status = 'End';
                        message.innerHTML = 'Game Over'.fontcolor('red') + '<br>Press Enter To Restart';
                        message.classList.add('messageStyle');
                        img.style.display = 'none';
                        die_sound.play();
                        return;
                    }
                } else {
                    if(graphics_attributes.right < pusheen_attributes.left && graphics_attributes.right + pusheen_speed >= pusheen_attributes.left && element.increase_score == '1'){
                        score_graphics.innerHTML = +score_graphics.innerHTML + 1;
                        score_sound.play();
                    }
                    element.style.left = graphics_attributes.left - pusheen_speed + 'px'; 
                }
            }
        });
        requestAnimationFrame(move);
    }
    requestAnimationFrame(move);
    let pusheen_velocity = 0;
    function apply_gravity(){
        if(game_status != 'Play') return;
        pusheen_velocity = pusheen_velocity + gravity;
        document.addEventListener('keydown', (e) => {
            if(e.key == ' '){
                pusheen_velocity = -7.6;
            }
        });
        if(pusheen_attributes.top <= 0 || pusheen_attributes.bottom >= background.bottom){
            game_status = 'End';
            message.style.left = '28vw';
            window.location.reload();
            message.classList.remove('messageStyle');
            return;
        }
        pusheen.style.top = pusheen_attributes.top + pusheen_velocity + 'px';
        pusheen_attributes = pusheen.getBoundingClientRect();
        requestAnimationFrame(apply_gravity);
    }
    requestAnimationFrame(apply_gravity);
    let pipes = 0;
    let pipe_gap = 35;
    function create_pipe(){
        if(game_status != 'Play') return;
        if(pipes > 115){
            pipes = 0;
            let pipe_position = Math.floor(Math.random() * 43) + 8;
            //inv = inverted
            let pipe_graphics_inv = document.createElement('div');
            pipe_graphics_inv.className = 'pipe_graphics';
            pipe_graphics_inv.style.top = pipe_position - 70 + 'vh';
            pipe_graphics_inv.style.left = '100vw';
            pipe_graphics_inv.style.height = '70vh'; 
            pipe_graphics_inv.style.width = '6vw';
            pipe_graphics_inv.style.backgroundImage = "url('images/toppipe.png')";
            pipe_graphics_inv.style.backgroundSize = 'cover';
            pipe_graphics_inv.style.backgroundRepeat = 'no-repeat';
            pipe_graphics_inv.style.backgroundPosition = 'bottom';
            document.body.appendChild(pipe_graphics_inv);
            let pipe_graphics = document.createElement('div');
            pipe_graphics.className = 'pipe_graphics';
            pipe_graphics.style.top = pipe_position + pipe_gap + 'vh';
            pipe_graphics.style.left = '100vw';
            pipe_graphics.style.height = '70vh';
            pipe_graphics.style.width = '6vw';
            pipe_graphics.style.backgroundImage = "url('images/bottompipe.png')";
            pipe_graphics.style.backgroundSize = 'cover';
            pipe_graphics.style.backgroundRepeat = 'no-repeat';
            pipe_graphics.increase_score = '1';
            document.body.appendChild(pipe_graphics);
            if(Math.random() < 0.3) { 
                let star_graphics = document.createElement('div');
                star_graphics.className = 'star_graphics';
                star_graphics.style.top = (pipe_position + pipe_gap / 2 + 2) + 'vh';
                star_graphics.style.left = '100vw'; 
                star_graphics.style.height = '4vh'; 
                star_graphics.style.width = '4vw'; 
                star_graphics.style.backgroundImage = "url('images/star.png')";
                star_graphics.style.backgroundSize = 'cover';
                star_graphics.style.backgroundRepeat = 'no-repeat';

                document.body.appendChild(star_graphics);
            }
        }
        pipes++;
        requestAnimationFrame(create_pipe);
    }
    requestAnimationFrame(create_pipe);
}
