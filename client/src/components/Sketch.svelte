<script>
    import P5 from 'p5-svelte';
    let width = 55;
    let height = 55;
  
    const sketch = (/** @type {{ setup: () => void; createCanvas: (arg0: number, arg1: number) => void; 
                    draw: () => void; ellipse: (arg0: number, arg1: number, arg2: number, arg3: number) => void;
                    width: number; height: number; }} */ p5) => {
      p5.setup = () => {
        p5.createCanvas(400, 400);
      };
  
      p5.draw = () => {
        p5.ellipse(p5.width / 2, p5.height / 2, width, height);
      };
    };
  </script>
  
  <label>
    Width
    <input type="range" bind:value={width} min="100" max="1000" step="0.01" />
    {width}
  </label>
  
  <label>
    Height
    <input type="range" bind:value={height} min="100" max="1000" step="0.01" />
    {height}
  </label>
  
  <P5 {sketch} />
  
  
  