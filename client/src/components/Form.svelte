<!-- Form.svelte -->
<script>
  let content = '';
  let musicInput = '';
  export let data = {};
  export let onSubmit = () => {}

  const submitForm = async () => {
    console.log("handling submit");
    try {
      const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content, musicInput })
      });
      console.log("here");
      console.log(response);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      data = await response.json();
      console.log(data);
      onSubmit(data);
      return data;
      // Handle response from server
    } catch (error) {
      console.error('Error:', error);
      return null;
      // Handle error
    }
   
  };
</script>

<div id='form' class='m-4 bg-emerald-500 content-center'>
  <form on:submit|preventDefault={submitForm}>
    <label>
      Name or Spotify link (Playlist requires link):
      <input type="text" id="content" bind:value={content}>
    </label>
    <br>

    <input type="radio" id="track" name="music_input" value="track" bind:group={musicInput}>
    <label for="track">Track</label><br>
    <input type="radio" id="album" name="music_input" value="album" bind:group={musicInput}>
    <label for="album">Album</label><br>
    <input type="radio" id="playlist" name="music_input" value="playlist" bind:group={musicInput}>
    <label for="Playlist">Playlist</label> 
    <br>

    <button type="submit">Submit</button>
  </form>

  <!-- <div>
    {JSON.stringify(data, null, 2)};
  </div> -->

</div>
