import React, { useEffect, useState } from 'react';
import BlogForm from './BlogForm';
import BlogPost from './BlogPost';

const BlogPage = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    // Fetch blog posts from the backend API
    const fetchPosts = async () => {
      const response = await fetch('/api/posts');
      const data = await response.json();
      setPosts(data);
    };

    fetchPosts();
  }, []);

  const handlePostCreate = (newPost) => {
    // Add the new post to the existing list of posts
    setPosts([...posts, newPost]);
  };

  const handlePostDelete = (postId) => {
    // Remove the deleted post from the list
    setPosts(posts.filter((post) => post.id !== postId));
  };

  return (
    <div className="blog-page">
      <header>
        <nav>
          {/* Your navigation menu goes here */}
        </nav>
      </header>
      <section className="blog-section">
        <div className="container">
          <h2>Blog</h2>
          <BlogForm onPostCreate={handlePostCreate} />
          {posts.map((post) => (
            <BlogPost key={post.id} post={post} onDelete={handlePostDelete} />
          ))}
        </div>
      </section>
      <footer>
        {/* Your footer goes here */}
      </footer>
    </div>
  );
};

export default BlogPage;
