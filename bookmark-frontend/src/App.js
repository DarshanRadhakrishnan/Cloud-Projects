import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Authenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import { fetchAuthSession } from 'aws-amplify/auth';

const API_URL = 'https://vkn0cfo0x6.execute-api.us-east-1.amazonaws.com/prod';

// 🔹 Component that runs ONLY after login
function AuthenticatedApp({ signOut, user }) {
  const [bookmarks, setBookmarks] = useState([]);
  const [title, setTitle] = useState('');
  const [url, setUrl] = useState('');

  // ✅ Hooks are allowed here
  useEffect(() => {
    fetchBookmarks();
  }, []);

  const fetchBookmarks = async () => {
    const session = await fetchAuthSession();
    const token = session.tokens.idToken.toString();

    const res = await axios.get(`${API_URL}/bookmarks`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    setBookmarks(res.data);
  };

  const addBookmark = async () => {
    const session = await fetchAuthSession();
    const token = session.tokens.idToken.toString();

    await axios.post(
      `${API_URL}/bookmarks`,
      { title, url },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    setTitle('');
    setUrl('');
    fetchBookmarks();
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Welcome {user.username}</h2>
      <button onClick={signOut}>Sign out</button>

      <h3>Add Bookmark</h3>
      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <br />
      <input
        placeholder="URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <br />
      <button onClick={addBookmark}>Add</button>

      <h3>Your Bookmarks</h3>
      <ul>
        {bookmarks.map((b) => (
          <li key={b.bookmarkId}>
            <a href={b.url} target="_blank" rel="noreferrer">
              {b.title}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

// 🔹 Auth wrapper ONLY (NO HOOKS HERE)
function App() {
  return (
    <Authenticator>
      {({ signOut, user }) => (
        <AuthenticatedApp signOut={signOut} user={user} />
      )}
    </Authenticator>
  );
}

export default App;
