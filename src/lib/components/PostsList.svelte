<script>
  export let posts = []
</script>


<ul class="posts-list">
  {#each posts as post}
    <script>
      export const load = async ({ params }) => {
		var ReadMeFile = await import(`/words/${post.slug}.md`);
    var ReadMe = ReadMeFile.default;
    export ReadMe
</script>
    <li>
      <article>
        <a href="/words/{post.slug}">
          <img
          src={post.coverImage}
          alt=""
          width={post.coverWidth}
          height={post.coverHeight}
          style="ratio: {post.coverWidth} / {post.coverHeight}"
          />
          <h2>
            {post.title}
          </h2>
        </a>
      </article>

      <p>{ReadMe}</p>
    </li>
  {/each}
</ul>