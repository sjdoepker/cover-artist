<script>
    import { onMount } from 'svelte';
    let content = '';
    let musicInput = '';
    const handleSubmit = async (/** @type {{ preventDefault: () => void; }} */ event) => {
        event.preventDefault(); // Prevent the default form submission behavior

        try {
        const response = await fetch('http://localhost:5000/', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content, musicInput })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log(data);
        // Handle response from server
        } catch (error) {
        console.error('Error:', error);
        // Handle error
    }
  };
</script>


<body class="m-4 content-center bg-emerald-200">
    <h1 class="text-green-3x1 font-bold underline">Welcome to spotty</h1>

    
        <div id='form' class=' m-4 bg-emerald-500 content-center'>
        <form method="POST">
            <label>
                Name or Spotify link (Playlist requires link)
                <input type="text" id="content" name="content">
            </label>
            <br>

            <input type="radio" id="track" name="music_input" value="track">
            <label for="track">Track</label><br>
            <input type="radio" id="album" name="music_input" value="album">
            <label for="album">Album</label><br>
            <input type="radio" id="playlist" name="music_input" value="Playlist">
            <label for="Playlist">Playlist</label> 
            <br>

            <button>Submit</button>
        </form>
    </div>
    </body>




