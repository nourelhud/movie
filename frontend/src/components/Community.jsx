import React, { useState, useEffect } from "react";
import axios from 'axios';
import Navbar from "./Navbar";
import Post from "./Post";
import CommentForm from"./CommentForm"
import "./Community.css"
import Footer from "./Footer";
function Community() {
  const [showCommentForm, setShowCommentForm] = useState(false);
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/posts/");
        const promises = response.data.map((post) =>
          axios.get(`http://127.0.0.1:8000/posts/${post.id}/comments/`)
        );
        const commentResponses = await Promise.all(promises);
        const postsWithComments = response.data.map((post, index) => ({
          ...post,
          comments: commentResponses[index].data,
        }));
        setPosts(postsWithComments);
        console.log(postsWithComments);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  }, []);

  const handlePostDelete = async (postId) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/posts/${postId}/delete/`);
      const updatedPosts = posts.filter((post) => post.id !== postId);
      setPosts(updatedPosts);
    } catch (error) {
      console.error(error);
    }
  };

  const handlePostCreated = (post) => {
    setPosts([...posts, post]);
    window.location.reload(true);
  };

  const handleCommentDelete = async (postId, commentId) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/posts/${postId}/comments/${commentId}/delete/`);
      const updatedPosts = posts.map((post) => {
        if (post.id === postId) {
          const updatedComments = post.comments.filter((comment) => comment.id !== commentId);
          return {
            ...post,
            comments: updatedComments,
          };
        } else {
          return post;
        }
      });
      setPosts(updatedPosts);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCommentCreated = (postId, comment) => {
    const updatedPosts = posts.map((post) => {
      if (post.id === postId) {
        return {
          ...post,
          comments: [...post.comments, comment],
        };
      } else {
        return post;
      }
    });
    setPosts(updatedPosts);
    window.location.reload(true);
  };
return (
  <>
    <Navbar />
    <>
      <Post onPostCreated={handlePostCreated} />
      <div className="contain">
        {posts.map((post) => (
          <>
            <div key={post.id}>
              <div className="post_body">
                <h4>Author: </h4>
                <span> {post.user?.name} </span>
                <span className="create_time">{post.created_at}</span>
                <button className="btn_del" onClick={() => handlePostDelete(post.id)}>Delete</button>
              </div>
              <div>
                <h3>Title:</h3>
                <h2>{post.title}</h2>
              </div>
              <h3>Content:</h3>
              <h2>{post.content}</h2> 
            </div>
            <div>
              {showCommentForm === post.id && (
                <CommentForm
                  postId={post.id}
                  onSubmit={(comment) =>
                    handleCommentCreated(post.id, comment)
                  }
                />
              )}
            </div>

            <div className="comment">
              <ul className="com">
                  <button className="add_btn" onClick={() => setShowCommentForm(post.id)}>
                    <i className="fas fa-comment-alt comment"></i> Add Comment
                  </button>
                {post.comments?.map((comment) => (
                  <div className="commentlist" key={comment.id}>
                    {comment.user && <h5>Commenter: <span>{comment.user?.name}</span> </h5>}
                    <div className="sec">
                    <p>{comment.content} </p>
                    <button className="btn_del" onClick={() => handleCommentDelete(post.id, comment.id)}>Delete</button>
                    </div>
                  </div>
                ))}
              </ul>
            </div>
            <hr />
          </>
        ))}
      </div>
    </>
    <Footer />
  </>
);
}

export default Community;