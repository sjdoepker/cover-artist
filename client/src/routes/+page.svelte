<script>
    import Form from "../components/Form.svelte";
    import Sketch from "../components/Sketch.svelte";
    /**
     * @type {string}
     */
    let submittedData = "";

</script>


<body class="m-4 align-middle bg-emerald-200">
    <h1 class="text-green-3x1 font-bold underline">Cover Artist</h1>    
        <Form onSubmit={(/** @type {string} */ data) => submittedData = data}/>

        <div>
            <span>Submitted Data</span>
            <pre>
                {JSON.stringify(submittedData, null, 2)}
            </pre>
            <Sketch />
            <!-- this is the feature data from the form! -->
        </div>
</body>




