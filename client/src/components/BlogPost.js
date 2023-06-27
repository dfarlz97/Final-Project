import React from 'react';

const BlogPost = ({ post, onDelete }) => {
  const handleDelete = async () => {
    // Send a DELETE request to the backend API to delete the blog post
    await fetch(`/api/posts/${post.id}`, { method: 'DELETE' });
    // Handle the response and any additional logic (e.g., removing the post from the UI)
    onDelete(post.id);
  };

  return (
    <div>
      <h3>{post.title}</h3>
      <p>{post.content}</p>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default BlogPost;
