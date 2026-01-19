document.getElementById('friendship-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const name1 = document.getElementById('name1').value.trim();
    const name2 = document.getElementById('name2').value.trim();

    if(!name1 || !name2) return;

    try {
        // const response = await fetch('http://localhost:5000/api/friendship', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify({ name1, name2 })
        // });

        // const data = await response.json();

        // document.getElementById('score').textContent = data.score;
        // document.getElementById('message').textContent = data.message;
        // document.getElementById('result').classList.remove('hidden');
        document.getElementById('friendship-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const score = 78; // temporary
        const message = "A strong bond filled with trust and memories ❤️"; // temporary
        document.getElementById('score').textContent = score;
        document.getElementById('message').textContent = message;
        document.getElementById('result').classList.remove('hidden');
        });


    } catch (err) {
        console.error("Error:", err);
        alert("Something went wrong! Please try again later.");
    }
});
