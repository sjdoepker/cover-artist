<script>
    import { onMount } from 'svelte';
    onMount(async() => {
        await getFeatures();
    })

    async function getFeatures() {

    }

</script>


<body class="m-12 content-center emerald-200">
        <h1 class="text-green-3x1 font-bold underline">Welcome to spotty</h1>
        <p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
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
    </body>




